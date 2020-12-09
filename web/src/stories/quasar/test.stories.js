import { QLayout, QPageContainer, QPage, QSelect, QBtn } from 'quasar'

export default {
  title: 'Quasar'
}

export const qInput = () => ({
  title: 'q-input',
  components: { QLayout, QPageContainer, QPage, QSelect, QBtn },
  template: `<q-layout>
    <q-page-container>
      <q-page class="full-height full-width justify-center items-center q-pa-xl">
        <div class="col-auto">
          <q-input v-model="name" label="Full name" />
          <q-list>
            <q-item>q-input: {{ name }}</q-item>
          </q-list>
        </div>
      </q-page>
    </q-page-container>
  </q-layout>`,
  data () {
    return {
      name: null,
      selected: null,
      role: 'User',
      options: ['Admin', 'Supervisor', 'User']
    }
  }
})

export const qSelect = () => ({
  title: 'q-select',
  components: { QLayout, QPageContainer, QPage, QSelect, QBtn },
  template: `<q-layout>
    <q-page-container>
      <q-page class="full-height full-width justify-center items-center q-pa-xl">
        <div class="col-auto">
          <q-select v-model="name" options="options">
          </q-select>
          <q-list>
            <q-item>q-input: {{ name }}</q-item>
          </q-list>
        </div>
      </q-page>
    </q-page-container>
  </q-layout>`,
  data () {
    return {
      name: null,
      role: 'User',
      options: ['Admin', 'Supervisor', 'User']
    }
  }
})
