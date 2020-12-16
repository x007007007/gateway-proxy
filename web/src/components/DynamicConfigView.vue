<template>
  <div>
    <div class="row fit justify-start wrap" v-for="i of ConfigItems" :key="i.id">
      <div class="col-12">
        <q-input
          v-if="i.isInput()"
          filled
          v-model="componentModels[i.name]"
          v-bind:aria-required="i.isRequired()"
          v-bind:label="i.displayName"
          v-bind:hint="i.displayName"
        />
        <q-toggle
          v-else-if="i.isToggle()"
          v-model="componentModels[i.name]"
          v-bind:label="i.displayName"
          v-bind:aria-required="i.isRequired()"
          v-bind:hint="i.displayName"
          color="yellow"
          left-label
        />
        <q-select
          v-else-if="i.isSwitch()"
          v-model="componentModels[i.name]"
          v-bind:label="i.displayName"
          v-bind:hint="i.displayName"
          :options="i.options"
          :option-label="(item) => item === null ? 'Null value' : item.name"
        />
        {{ componentModels[i.name] }}

      </div>
      <div
        class="offset-1 col-11"
        v-if="i.isSwitch() && componentModels[i.name] && componentModels[i.name].have_sub_config" >
        <DynamicConfigView
          v-model="subRes[i.name]"
          :config-id="configId"
          :table-id="componentModels[i.name].id"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { InputData } from './help'

export default {
  name: 'DynamicConfigView',
  props: {
    value: {
      type: Object,
      default: function () {
        return {}
      }
    },
    configId: {
      type: Number,
      required: true
    },
    tableId: {
      type: Number,
      required: false
    }
  },
  data: function () {
    return {
      subRes: {},
      componentModels: {},
      ConfigItems: []
    }
  },
  watch: {
    subRes: {
      handler () {
        this.popupModel()
      },
      deep: true,
      immediate: true
    },
    componentModels: {
      handler () {
        this.popupModel()
      },
      deep: true,
      immediate: true
    },
    tableId () {
      this.refresh()
    }
  },
  methods: {
    async GetList () {
      console.log(this.cnnfigId, this.tableId)
      const resp = await this.$axios.get(`/api/config/type/${this.configId}/table/`, {
        params: {
          id: this.tableId
        }
      })
      const res = resp.data.map((i) => {
        return new InputData(i)
      })
      console.log(res)
      this.ConfigItems = res
    },
    refresh () {
      this.GetList()
    },
    popupModel () {
      // 向上传播 model 数据结构
      const res = {}
      Object.entries(this.componentModels).forEach(([k, v]) => {
        res[k] = v
      })
      Object.entries(this.subRes).forEach(([k, v]) => {
        res[k] = {
          id: res[k],
          sub: v
        }
      })
      this.$emit('input', res)
      return res
    }
  },
  created () {
    this.refresh()
  }
}
</script>
