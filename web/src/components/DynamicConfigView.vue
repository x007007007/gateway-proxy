<template>
  <div>
    <div class="row fit justify-start wrap" v-for="i of propConfigItems" :key="i.id">
      <dynamic-config-list-warp
        :is-list="true"
        class="col-12">
        <template slot-scope="props">
          <q-input
            v-if="i.isInput()"
            filled
            v-model="props.compModelMap[i.name]"
            v-bind:aria-required="i.isRequired()"
            v-bind:label="i.displayName"
            v-bind:hint="i.displayName"
          />
          <q-toggle
            v-else-if="i.isToggle()"
            v-model="props.compModelMap[i.name]"
            v-bind:label="i.displayName"
            v-bind:aria-required="i.isRequired()"
            v-bind:hint="i.displayName"
            color="yellow"
            left-label
          />
          <q-select
            v-else-if="i.isSwitch()"
            v-model="props.subGroupSelectedIdMap[i.name]"
            v-bind:label="i.displayName"
            v-bind:hint="i.displayName"
            :options="i.options"
            :option-label="(item) => item === null ? 'Null value' : item.name"
          />
        </template>
      </dynamic-config-list-warp>
      <dynamic-config-list-warp
        :is-list="false"
        class="offset-1 col-11"
        v-if="i.isSwitch() && subGroupSelectedIdMap[i.name] && subGroupSelectedIdMap[i.name].have_sub_config && subGroupConfCompListMap[i.name]" >
        <template slot-scope="props">
          <DynamicConfigView
            v-model="props.subGroupCompModelMap[i.name]"
            :parent-key="props.subGroupSelectedIdMap[i.name]"
            :config-items="props.subGroupConfCompListMap[i.name]"
            :config-id="configId"
            :table-id="props.subGroupSelectedIdMap[i.name].id"
          />
        </template>
      </dynamic-config-list-warp>
    </div>
  </div>
</template>

<script>
import { InputData } from './help'
import Vue from 'vue'
import DynamicConfigListWarp from 'components/DynamicConfigListWarp'

export default {
  name: 'DynamicConfigView',
  components: { DynamicConfigListWarp },
  directives: {
    isListed: {
      bind (el, { name, value, oldValue, expression, arg, oldArg, modifiers }, vnode) {
        console.log(name, value, oldValue, expression, arg, oldArg, modifiers)
        if (value === true) {
          console.log(vnode)
          console.log(el)
        }
      },
      inserted (el) {
        console.log(el)
      }

    }
  },
  props: {
    value: {
      type: Object,
      default: function () {
        return {}
      }
    },
    parentKey: {
      required: false
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
      compModelMap: {}
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
        init.compModelMap[item.name] = this.value[item.name]
      }
    }

    return init
  },
  watch: {
    parentKey: {
      handler () {
        console.log('parent key change')
        this.popupModel()
      },
      deep: true,
      immediate: false
    },
    subGroupCompModelMap: {
      handler () {
        this.popupModel()
      },
      deep: true,
      immediate: false
    },
    compModelMap: {
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
      for (const itemName in subGroupSelectedMap) { // 选项名
        const res = await this.GetList({ configId: this.configId, tableId: subGroupSelectedMap[itemName].id })
        Vue.set(this.subGroupConfCompListMap, itemName, res)
        // Vue.set(this.subGroupCompModelMap, itemName, {})
      }
    },
    popupModel () {
      // 向上传播 model 数据结构
      const res = {}
      Object.entries(this.compModelMap).forEach(([k, v]) => {
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
