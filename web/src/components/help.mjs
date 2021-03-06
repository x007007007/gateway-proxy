export class InputData {
  constructor (data) {
    this.data = data
  }

  get name () {
    return this.data.name
  }

  get options () {
    return this.data.items
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

  get componentName () {
    return {
      string: "q-input",
      int: "q-input",
      bool: "q-toggle"

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
