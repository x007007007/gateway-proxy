<template>
  <div>
    <q-btn
      color="primary"
      size="md"
      @click="add()"
    />
    <ul v-if="isList">
      <li v-for="[offset, v] in stack.entries()" :key="offset">
        <slot
          :subGroupCompModelMap="v.subGroupCompModelMap"
          :subGroupSelectedIdMap="v.subGroupSelectedIdMap"
          :compModelMap="v.compModelMap"
        >
        </slot>
      </li>
    </ul>
    <slot v-else ></slot>
  </div>
</template>

<script>
export default {
  name: 'DynamicConfigListWarp',
  props: {
    isList: {
      type: Boolean,
      required: true
    },
    value: {
      type: [Array, Object],
      default () {
        if (this.isList) {
          return []
        } else {
          return {}
        }
      }
    }
  },
  data () {
    const init = {
      subGroupCompModelMap: []
    }
    if (this.isList) {
      init.stack = []
    } else {
      init.model = {}
    }
    return init
  },
  methods: {
    add () {
      console.log('add')
      if (this.isList) {
        this.stack.push({
          subGroupCompModelMap: {},
          subGroupConfCompListMap: {}, // api callback成功后创建
          subGroupSelectedIdMap: {},
          compModelMap: {}
        })
      }
    },
    generateModel (dataMeta) {
      // 向上传播 model 数据结构
      const res = {}
      Object.entries(dataMeta.compModelMap).forEach(([k, v]) => {
        res[k] = v
      })
      Object.entries(dataMeta.subGroupSelectedIdMap).forEach(([k, v]) => {
        res[k] = {
          id: v,
          sub: dataMeta.subGroupCompModelMap[k]
        }
      })
      return res
    },
    popupModel () {
      if (this.isList) {
        const model = this.stack.map(tgis.generateModel)
      } else {
        const model = this.generateModel(this.model)
      }
    }
  }
}
</script>

<style scoped>

</style>
