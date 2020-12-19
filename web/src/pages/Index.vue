<template>
  <q-page class="flex flex-center">
    <q-form class="fit q-ma-md q-pa-md">
      <div >
        <DynamicConfigView
          v-if="configItems"
          :config-id="1"
          v-model="res"
          :configItems="configItems"
        />
      </div>
    </q-form>
  </q-page>
</template>

<script>
import DynamicConfigView from 'components/DynamicConfigView'
import { InputData } from 'components/help'

const conf = '{ "addr": "00000000", "port": "999", "fast_tcp": true, "plugin": { "id": { "id": 5, "name": "v2ray", "have_sub_config": true }, "sub": { "mode": { "id": { "id": 10, "name": "http2", "have_sub_config": true }, "sub": { "path": "9999", "insecurity": true, "peername": "kkkkk", "host": "88888" } } } } } '

export default {
  name: 'PageIndex',
  components: {
    DynamicConfigView
  },
  data () {
    return {
      res: JSON.parse(conf),
      configItems: null
    }
  },
  methods: {
    async GetList ({ configId, tableId }) {
      let resp
      if (tableId) {
        resp = await this.$axios.get(`/api/config/type/${configId}/schema/`, {
          params: {
            id: tableId
          }
        })
      } else {
        resp = await this.$axios.get(`/api/config/type/${configId}/schema/`)
      }
      return resp.data.map((i) => {
        return new InputData(i)
      })
    }
  },
  created () {
    this.GetList({ configId: 1 }).then((res) => {
      this.configItems = res
    })
  }
}
</script>
