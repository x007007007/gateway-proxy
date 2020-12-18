<template>
  <div>
    <div class="row fit justify-start wrap" v-for="i of propConfigItems" :key="i.id">
      <div class="col-12">
        <q-input
          v-if="i.isInput()"
          filled
          v-model="subCompModelMap[i.name]"
          v-bind:aria-required="i.isRequired()"
          v-bind:label="i.displayName"
          v-bind:hint="i.displayName"
        />
        <q-toggle
          v-else-if="i.isToggle()"
          v-model="subCompModelMap[i.name]"
          v-bind:label="i.displayName"
          v-bind:aria-required="i.isRequired()"
          v-bind:hint="i.displayName"
          color="yellow"
          left-label
        />
        <q-select
          v-else-if="i.isSwitch()"
          v-model="subGroupSelectedIdMap[i.name]"
          v-bind:label="i.displayName"
          v-bind:hint="i.displayName"
          :options="i.options"
          :option-label="(item) => item === null ? 'Null value' : item.name"
        />
      </div>
      <div
        class="offset-1 col-11"
        v-if="i.isSwitch() && subGroupSelectedIdMap[i.name] && subGroupSelectedIdMap[i.name].have_sub_config && subGroupConfCompListMap[i.name]" >
        <DynamicConfigView
          v-model="subGroupCompModelMap[i.name]"
          :config-items="subGroupConfCompListMap[i.name]"
          :config-id="configId"
          :table-id="subGroupSelectedIdMap[i.name].id"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { InputData } from './help'
import Vue from 'vue'

export default {
  name: 'DynamicConfigView',
  props: {
    value: {
      type: Object,
      default: function () {
        return {}
      }
    },
    configItems: {
      type: Array,
      required: true
    },
    subQueryArg: {
      type: Object
    },
    configId: {
      type: Number,
      required: true
    }
  },
  computed: {
    propConfigItems () {
      return this.configItems
    }
  },
  data () {
    const init = {
      subGroupCompModelMap: {},
      subGroupConfCompListMap: {}, // api callback成功后创建
      subGroupSelectedIdMap: {},
      subCompModelMap: {}
    }
    for (const item of this.configItems) {
      if (item.isSwitch() && this.value && this.value[item.name]) { // 是子组
        init.subGroupCompModelMap[item.name] = this.value[item.name].sub
        init.subGroupSelectedIdMap[item.name] = this.value[item.name].id
        if (this.value[item.name].id) {
          this.GetList({ configId: this.configId, tableId: init.subGroupSelectedIdMap[item.name].id }).then((res) => {
            Vue.set(this.subGroupConfCompListMap, item.name, res)
          })
        }
      } else {
        init.subCompModelMap[item.name] = this.value[item.name]
      }
    }

    return init
  },
  watch: {
    subGroupCompModelMap: {
      handler () {
        this.popupModel()
      },
      deep: true,
      immediate: false
    },
    subCompModelMap: {
      handler () {
        this.popupModel()
      },
      deep: true,
      immediate: false
    },
    subGroupSelectedIdMap: {
      async handler (v1, v2) { // 修改 子组建配置参数
        await this.updateSubGroupCompMap(v1)
        this.popupModel()
      },
      deep: true,
      immediate: false
    }
  },
  methods: {
    async GetList ({ configId, tableId }) {
      const resp = await this.$axios.get(`/api/config/type/${configId}/schema/`, {
        params: {
          id: tableId
        }
      })
      return resp.data.map((i) => {
        return new InputData(i)
      })
    },
    async updateSubGroupCompMap (subGroupSelectedMap) {
      for (const itemName in subGroupSelectedMap) {
        const res = await this.GetList({ configId: this.configId, tableId: subGroupSelectedMap[itemName].id })
        Vue.set(this.subGroupConfCompListMap, itemName, res)
        this.subGroupCompModelMap[itemName] = {}
      }
    },
    popupModel () {
      // 向上传播 model 数据结构
      const res = {}
      Object.entries(this.subCompModelMap).forEach(([k, v]) => {
        res[k] = v
      })
      Object.entries(this.subGroupSelectedIdMap).forEach(([k, v]) => {
        res[k] = {
          id: v,
          sub: this.subGroupCompModelMap[k]
        }
      })
      this.$emit('input', res)
      return res
    }
  },
  created () {

  }
}
</script>
