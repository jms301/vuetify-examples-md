# Vuetify component v-radio-group - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <div>
      <v-radio-group v-bind="props" hide-details>
        <v-radio label="Radio One" value="one"></v-radio>
        <v-radio label="Radio Two" value="two"></v-radio>
        <v-radio label="Radio Three" value="three"></v-radio>
      </v-radio-group>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="label" label="Radio group label"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-radio-group'
  const model = ref('default')
  const options = ['inline']
  const label = ref(false)
  const props = computed(() => {
    return {
      inline: model.value === 'inline' || undefined,
      label: label.value ? 'Radio group label' : undefined,
    }
  })

  const slots = computed(() => {
    return `
  <v-radio label="Radio One" value="one"></v-radio>
  <v-radio label="Radio Two" value="two"></v-radio>
  <v-radio label="Radio Three" value="three"></v-radio>
`
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-radio-group - prop model radio

Example code

```vue
<template>
  <v-container fluid>
    <v-select
      v-model="radio"
      :items="['Option 1', 'Option 2']"
      label="Select Option"
    ></v-select>
    <v-radio
      v-model="radio"
      false-value="Option 2"
      label="Option 1"
      true-value="Option 1"
      readonly
    ></v-radio>
    <v-radio
      v-model="radio"
      false-value="Option 1"
      label="Option 2"
      true-value="Option 2"
      readonly
    ></v-radio>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const radio = ref('Option 1')
</script>

<script>
  export default {
    data () {
      return {
        radio: 'Option 1',
      }
    },
  }
</script>

```

# Vuetify component v-radio-group - prop direction

Example code

```vue
<template>
  <v-container fluid>
    <v-radio-group v-model="column">
      <v-radio
        label="Option 1"
        value="radio-1"
      ></v-radio>
      <v-radio
        label="Option 2"
        value="radio-2"
      ></v-radio>
    </v-radio-group>
    <hr>
    <v-radio-group
      v-model="inline"
      inline
    >
      <v-radio
        label="Option 1"
        value="radio-1"
      ></v-radio>
      <v-radio
        label="Option 2"
        value="radio-2"
      ></v-radio>
    </v-radio-group>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const column = ref(null)
  const inline = ref(null)
</script>

<script>
  export default {
    data () {
      return {
        column: null,
        inline: null,
      }
    },
  }
</script>

```

# Vuetify component v-radio-group - prop model group

Example code

```vue
<template>
  <v-container fluid>
    <p>Selected Button: {{ radios }}</p>
    <v-radio-group v-model="radios">
      <v-radio label="Option One" value="one"></v-radio>
      <v-radio label="Option 2 (string)" value="2"></v-radio>
      <v-radio :value="3" label="Option 3 (integer)"></v-radio>
    </v-radio-group>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const radios = ref('one')
</script>

<script>
  export default {
    data () {
      return {
        radios: 'one',
      }
    },
  }
</script>

```

# Vuetify component v-radio-group - prop colors

Example code

```vue
<template>
  <v-card flat>
    <v-card-text>
      <v-container fluid>
        <v-row>
          <v-col
            cols="12"
            md="6"
            sm="6"
          >
            <v-radio-group v-model="ex7">
              <v-radio
                color="red"
                label="red"
                value="red"
              ></v-radio>
              <v-radio
                color="red-darken-3"
                label="red-darken-3"
                value="red-darken-3"
              ></v-radio>
              <v-radio
                color="indigo"
                label="indigo"
                value="indigo"
              ></v-radio>
              <v-radio
                color="indigo-darken-3"
                label="indigo-darken-3"
                value="indigo-darken-3"
              ></v-radio>
              <v-radio
                color="orange"
                label="orange"
                value="orange"
              ></v-radio>
              <v-radio
                color="orange-darken-3"
                label="orange-darken-3"
                value="orange-darken-3"
              ></v-radio>
            </v-radio-group>
          </v-col>
          <v-col
            cols="12"
            md="6"
            sm="6"
          >
            <v-radio-group v-model="ex8">
              <v-radio
                color="primary"
                label="primary"
                value="primary"
              ></v-radio>
              <v-radio
                color="secondary"
                label="secondary"
                value="secondary"
              ></v-radio>
              <v-radio
                color="success"
                label="success"
                value="success"
              ></v-radio>
              <v-radio
                color="info"
                label="info"
                value="info"
              ></v-radio>
              <v-radio
                color="warning"
                label="warning"
                value="warning"
              ></v-radio>
              <v-radio
                color="error"
                label="error"
                value="error"
              ></v-radio>
            </v-radio-group>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const ex7 = ref('red')
  const ex8 = ref('primary')
</script>

<script>
  export default {
    data () {
      return {
        ex7: 'red',
        ex8: 'primary',
      }
    },
  }
</script>

```

# Vuetify component v-radio-group - slot label

Example code

```vue
<template>
  <v-container fluid>
    <v-radio-group v-model="radios">
      <template v-slot:label>
        <div>Your favourite <strong>search engine</strong></div>
      </template>
      <v-radio value="Google">
        <template v-slot:label>
          <div>Of course it's <strong class="text-success">Google</strong></div>
        </template>
      </v-radio>
      <v-radio value="Duckduckgo">
        <template v-slot:label>
          <div>Definitely <strong class="text-primary">Duckduckgo</strong></div>
        </template>
      </v-radio>
    </v-radio-group>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const radios = ref('Duckduckgo')
</script>

<script>
  export default {
    data () {
      return {
        radios: 'Duckduckgo',
      }
    },
  }
</script>

```
