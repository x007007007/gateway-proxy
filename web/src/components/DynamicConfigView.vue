<template>
  <q-item>
    <q-item-section v-for="i in ConfigItems" :key="i.id">
      <q-item-label>{{ i.name }}</q-item-label>
      <q-item-label caption>
        {{ i }}
      </q-item-label>
    </q-item-section>
  </q-item>
</template>

<script>
export default {
  name: 'DynamicConfigView',
  data: function () {
    return {
      ConfigItems: [

      ]
    }
  },
  props: {
    type: {
      type: Intl,
      required: true
    }
  },
  methods: {
    async GetList (typeId) {
      const res = await this.$axios.get(`/api/config/type/${typeId}/table/`, {
      })
      this.ConfigItems = res
    }
  },
  created () {
    this.GetList(1).then(
      function () {
        console.log(arguments)
      }
    )
  }
}
</script>
