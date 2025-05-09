# Vuetify component v-number-input - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <div class="text-center">
      <v-number-input v-bind="props"></v-number-input>
    </div>

    <template v-slot:configuration>
      <v-select
        v-model="controlVariant"
        :items="controlVariantOptions"
        label="Control Variant"
      ></v-select>
      <v-checkbox v-model="reverse" label="Reverse"></v-checkbox>
      <v-checkbox v-model="inset" label="Inset"></v-checkbox>
      <v-checkbox v-model="hideInput" label="HideInput"></v-checkbox>
      <v-text-field v-model="label" label="Label" clearable></v-text-field>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = ref('v-number-input')
  const model = ref('default')
  const options = ['outlined', 'filled', 'solo', 'solo-inverted', 'solo-filled']
  const controlVariantOptions = ['default', 'stacked', 'split']
  const reverse = ref(false)
  const controlVariant = ref('default')
  const disabled = ref(false)
  const loading = ref(false)
  const inset = ref(false)
  const hideInput = ref(false)
  const label = ref('')

  const props = computed(() => {
    return {
      reverse: reverse.value,
      controlVariant: controlVariant.value,
      disabled: disabled.value || undefined,
      label: label.value,
      loading: loading.value || undefined,
      hideInput: hideInput.value,
      inset: inset.value,
      variant: model.value !== 'default' ? model.value : undefined,
    }
  })

  const slots = computed(() => {
    return ``
  })

  const code = computed(() => {
    return `<v-number-input${propsToString(props.value)}>${slots.value}</v-number-input>`
  })
</script>

```

# Vuetify component v-number-input - prop control variant

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="4" sm="4">
        <h5>Default</h5>

        <v-number-input control-variant="default"></v-number-input>
      </v-col>

      <v-col cols="12" md="4" sm="4">
        <h5>Stacked</h5>

        <v-number-input control-variant="stacked"></v-number-input>
      </v-col>

      <v-col cols="12" md="4" sm="4">
        <h5>Split</h5>

        <v-number-input control-variant="split"></v-number-input>
      </v-col>

      <v-col cols="12" md="4" sm="4">
        <h5>Hidden</h5>

        <v-number-input control-variant="hidden"></v-number-input>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-number-input - prop hide input

Example code

```vue
<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="auto">
        <v-number-input variant="outlined" hide-details hide-input></v-number-input>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-number-input - prop precision

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col>
        <h5>(default precision="0")</h5>
        <v-number-input v-model="example1" :precision="0" hide-details="auto"></v-number-input>
        <code class="d-block pt-3">value: {{ example1 }}</code>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h5>(precision="2")</h5>
        <v-number-input v-model="example2" :precision="2" hide-details="auto"></v-number-input>
        <code class="d-block pt-3">value: {{ example2 }}</code>
      </v-col>
      <v-col>
        <h5>(precision="5")</h5>
        <v-number-input v-model="example3" :precision="5" hide-details="auto"></v-number-input>
        <code class="d-block pt-3">value: {{ example3 }}</code>
      </v-col>
      <v-col>
        <h5>(precision unrestricted)</h5>
        <v-number-input v-model="example4" :precision="null" hide-details="auto"></v-number-input>
        <code class="d-block pt-3">value: {{ example4 }}</code>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const example1 = ref(4.052)
  const example2 = ref(123)
  const example3 = ref(25.5)
  const example4 = ref(0.052)
</script>

<script>
  export default {
    data: () => ({
      example1: 4.052,
      example2: 123,
      example3: 25.5,
      example4: 0.052,
    }),
  }
</script>

```

# Vuetify component v-number-input - prop min max

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col>
        <h5>min:10/max:20</h5>

        <v-number-input
          :max="20"
          :min="10"
          :model-value="15"
        ></v-number-input>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-number-input - prop reverse

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="4" sm="4">
        <h5>Default</h5>

        <v-number-input
          control-variant="default"
          reverse
        ></v-number-input>
      </v-col>

      <v-col cols="12" md="4" sm="4">
        <h5>Stacked</h5>

        <v-number-input
          control-variant="stacked"
          reverse
        ></v-number-input>
      </v-col>

      <v-col cols="12" md="4" sm="4">
        <h5>Split</h5>

        <v-number-input
          control-variant="split"
        ></v-number-input>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-number-input - prop inset

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="6">
        <h5>Default</h5>

        <v-number-input
          control-variant="default"
          inset
        ></v-number-input>
      </v-col>

      <v-col cols="12" sm="6">
        <h5>Stacked</h5>

        <v-number-input
          control-variant="stacked"
          inset
        ></v-number-input>
      </v-col>

      <v-col cols="12" sm="6">
        <h5>Split</h5>

        <v-number-input
          control-variant="split"
          inset
        ></v-number-input>
      </v-col>

      <v-col cols="12" sm="6">
        <h5>Hide-input</h5>

        <v-number-input
          hide-input
          inset
        ></v-number-input>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-number-input - prop step

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col>
        <h5>step 2; min:10; max:20</h5>

        <v-number-input
          :max="20"
          :min="10"
          :model-value="15"
          :step="2"
        ></v-number-input>
      </v-col>
    </v-row>
  </v-container>
</template>

```
