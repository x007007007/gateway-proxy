<template>
  <q-page class="flex flex-center">
    <q-form class="fit q-ma-md q-pa-md">
     res {{ res }}
      <DynamicConfigView :config-id="1" v-model="res" />
    </q-form>
  </q-page>
</template>

<script>
import DynamicConfigView from 'components/DynamicConfigView'
export default {
  name: 'PageIndex',
  components: {
    DynamicConfigView
  },
  data () {
    return {
      res: {}
    }
  }
}
</script>
