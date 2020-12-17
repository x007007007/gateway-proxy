<template>
  <q-page class="flex flex-center">
    <q-form class="fit q-ma-md q-pa-md">
     res {{ res }}
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

export default {
  name: 'PageIndex',
  components: {
    DynamicConfigView
  },
  data () {
    return {
      res: JSON.parse('{ "addr": "sssss", "plugin": { "id": { "id": 3, "name": "v2ray", "have_sub_config": true }, "sub": { "mode": { "id": { "id": 7, "name": "http2", "have_sub_config": true }, "sub": { "peername": "ssss", "tls": true } } } } } '),
      configItems: null
    }
  },
  methods: {
    async GetList ({ configId, tableId }) {
      let resp
      if (tableId) {
        resp = await this.$axios.get(`/api/config/type/${configId}/table/`, {
          params: {
            id: tableId
          }
        })
      } else {
        resp = await this.$axios.get(`/api/config/type/${configId}/table/`)
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
