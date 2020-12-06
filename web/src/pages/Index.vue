<template>
  <q-page class="flex flex-center">
    <q-form>
      <DynamicConfigView :config-id="1" />
    </q-form>
  </q-page>
</template>

<script>
import DynamicConfigView from 'components/DynamicConfigView'
export default {
  name: 'PageIndex',
  components: {
    DynamicConfigView
  }
}
</script>
