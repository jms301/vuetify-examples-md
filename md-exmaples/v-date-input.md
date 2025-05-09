# Vuetify component v-date-input - usage

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
      <v-date-input v-bind="props"></v-date-input>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="clear" label="Clearable"></v-checkbox>

      <v-checkbox v-model="disabled" label="Disabled"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-date-input'
  const model = ref('default')
  const options = ['outlined', 'underlined', 'solo', 'solo-filled', 'solo-inverted']
  const clear = ref(false)
  const counter = ref(false)
  const disabled = ref(false)
  const props = computed(() => {
    return {
      clearable: clear.value || undefined,
      counter: counter.value || undefined,
      disabled: disabled.value || undefined,
      label: 'Date input',
      variant: model.value === 'default' ? undefined : model.value,
    }
  })

  const slots = computed(() => {
    return ``
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-date-input - prop multiple

Example code

```vue
<template>
  <div class="d-flex justify-center">
    <v-date-input
      v-model="model"
      label="Select day(s)"
      max-width="368"
      multiple
    ></v-date-input>
  </div>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const model = shallowRef(null)
</script>

<script>
  export default {
    data: () => ({
      model: null,
    }),
  }
</script>

```

# Vuetify component v-date-input - misc passenger

Example code

```vue
<template>
  <v-card class="mx-auto" max-width="420">
    <v-layout>
      <v-system-bar color="#4603c0">
        <v-icon icon="mdi-square"></v-icon>

        <v-icon icon="mdi-circle"></v-icon>

        <v-icon icon="mdi-triangle"></v-icon>
      </v-system-bar>

      <v-app-bar color="#6200ee" title="Passenger information" flat>
        <template v-slot:prepend>
          <v-btn icon="mdi-arrow-left"></v-btn>
        </template>
      </v-app-bar>

      <v-main>
        <v-container class="pt-8">
          <v-text-field
            label="Name"
            model-value="John Leider"
            variant="outlined"
          ></v-text-field>

          <v-date-input
            label="Date of birth"
            prepend-icon=""
            variant="outlined"
            persistent-placeholder
          ></v-date-input>

          <v-text-field label="Address" variant="outlined"></v-text-field>
          <v-text-field label="City" variant="outlined"></v-text-field>

          <div class="d-flex ga-2">
            <v-text-field label="State" variant="outlined"></v-text-field>

            <v-text-field label="Zip code" variant="outlined"></v-text-field>
          </div>
        </v-container>
      </v-main>
    </v-layout>

    <template v-slot:actions>
      <v-btn color="#4603c0" disabled>Prev</v-btn>

      <v-spacer></v-spacer>

      <v-btn color="#4603c0">Next</v-btn>
    </template>
  </v-card>
</template>

```

# Vuetify component v-date-input - prop prepend icon

Example code

```vue
<template>
  <v-row dense>
    <v-col cols="12" md="6">
      <v-date-input
        label="Select a date"
        prepend-icon=""
        prepend-inner-icon="$calendar"
        variant="solo"
      ></v-date-input>
    </v-col>

    <v-col cols="12" md="6">
      <v-date-input
        label="Select a date"
        prepend-icon=""
        variant="solo"
      ></v-date-input>
    </v-col>
  </v-row>
</template>

```

# Vuetify component v-date-input - prop model

Example code

```vue
<template>
  <div class="d-flex justify-center">
    <v-date-input
      v-model="model"
      label="Select a date"
      max-width="368"
    ></v-date-input>
  </div>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const model = shallowRef(null)
</script>

<script>
  export default {
    data: () => ({
      model: null,
    }),
  }
</script>

```

# Vuetify component v-date-input - prop multiple range

Example code

```vue
<template>
  <div class="d-flex justify-center">
    <v-date-input
      v-model="model"
      label="Select range"
      max-width="368"
      multiple="range"
    ></v-date-input>
  </div>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const model = shallowRef(null)
</script>

<script>
  export default {
    data: () => ({
      model: null,
    }),
  }
</script>

```

# Vuetify component v-date-input - prop display format

Example code

```vue
<template>
  <div class="d-flex justify-center">
    <v-date-input
      v-model="model"
      :display-format="format"
      max-width="368"
      prefix="ISO Date:"
    ></v-date-input>
  </div>
</template>

<script setup>
  import { shallowRef } from 'vue'
  import { useDate } from 'vuetify'

  const adapter = useDate()
  const model = shallowRef(adapter.parseISO('2025-02-25'))

  function format (date) {
    return adapter.toISO(date)
  }
</script>

```
