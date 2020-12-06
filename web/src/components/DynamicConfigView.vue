<template>
  <div>
    <div v-for="i of ConfigItems" :key="i.id">
      <q-input
        v-if="i.isInput()"
        filled
        v-model="userInput[i.name]"
        v-bind:aria-required="i.isRequired()"
        v-bind:label="i.displayName"
        v-bind:hint="i.displayName"
      />
      <q-toggle
        v-else-if="i.isToggle()"
        v-model="userInput[i.name]"
        v-bind:label="i.displayName"
        v-bind:aria-required="i.isRequired()"
        v-bind:hint="i.displayName"
        color="yellow"
        left-label
      />
      <q-select
        v-else-if="i.isSwitch()"
        v-model="userInput[i.name]"
        v-bind:label="i.displayName"
        v-bind:hint="i.displayName"
        :options="i.options"
        :option-label="(item) => item === null ? 'Null value' : item.name"
        @input="selectOptions"
      />
      <div v-if="i.isSwitch() && userInput[i.name] && userInput[i.name].have_sub_config" >
        <DynamicConfigView
          :config-id="configId"
          :table-id="userInput[i.name].id"
        />
      </div>
    </div>
  </div>
</template>

<script>
class InputData {
  constructor (data) {
    this.data = data
    console.log(data)
  }

  get name () {
    return this.data.name
  }

  get options () {
    return this.data.switch
  }

  get displayName () {
    return this.data.display_name
  }

  get type () {
    console.log('hi')
    return {
      string: 'String',
      int: 'Integer',
      float: 'Number'
    }[this.data.type]
  }

  get id () {
    return this.data.id
  }

  isInput () {
    for (const i of ['string', 'float', 'int']) {
      if (this.data.type === i) {
        return true
      }
    }
    return false
  }

  isToggle () {
    return this.data.type === 'bool'
  }

  isRequired () {
    return this.data.required
  }

  isSwitch () {
    return this.data.type === 'switch'
  }
}

export default {
  name: 'DynamicConfigView',
  data: function () {
    return {
      ConfigItems: [

      ],
      userInput: {}
    }
  },
  props: {
    configId: {
      type: Number,
      required: true
    },
    tableId: {
      type: Number,
      required: false
    }
  },
  watch: {
    $props: {
      handler () {
        this.refresh()
      },
      deep: true,
      immediate: true
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
    selectOptions () {
      console.log('hello world', arguments)
    },
    refresh () {
      this.GetList().then(
        function () {
          console.log(arguments)
        }
      )
    }
  },
  created () {
    this.refresh()
  }
}
</script>
