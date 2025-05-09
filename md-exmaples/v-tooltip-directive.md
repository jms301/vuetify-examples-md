# Vuetify component v-tooltip-directive - usage

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
      <v-btn :key="text" text="Tooltip" v-tooltip="text"></v-btn>
    </div>

    <template v-slot:configuration>
      <v-text-field v-model="text" label="Text"></v-text-field>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-tooltip'
  const model = ref('default')
  const text = ref('Tooltip')
  const options = []

  const code = computed(() => {
    return `<v-btn v-tooltip="'${text.value}'"></v-btn>`
  })
</script>

```

# Vuetify component v-tooltip-directive - object literals

Example code

```vue
<template>
  <div class="text-center py-10">
    <v-btn text="Click me" v-tooltip="tooltip"></v-btn>
  </div>
</template>

<script setup>
  const tooltip = {
    text: 'Scroll up ↑',
    scrollStrategy: 'close',
    scrim: true,
    persistent: false,
    openOnClick: true,
    openOnHover: false,
  }
</script>

<script>
  export default {
    data: () => ({
      tooltip: {
        text: 'Scroll up ↑',
        scrollStrategy: 'close',
        scrim: true,
        persistent: false,
        openOnClick: true,
        openOnHover: false,
      },
    }),
  }
</script>

```

# Vuetify component v-tooltip-directive - args

Example code

```vue
<template>
  <div class="d-flex justify-center ga-4 py-10">
    <v-btn v-tooltip:start="'Tooltip at the start'">
      Start
    </v-btn>

    <v-btn v-tooltip:end="'Tooltip at the end'">
      End
    </v-btn>

    <v-btn v-tooltip:top="'Tooltip at the top'">
      Top
    </v-btn>

    <v-btn v-tooltip:bottom="'Tooltip at the bottom'">
      Bottom
    </v-btn>

    <v-btn v-tooltip:bottom-end="'Tooltip at the bottom end'">
      Bottom end
    </v-btn>
  </div>
</template>

```

# Vuetify component v-tooltip-directive - text

Example code

```vue
<template>
  <div class="d-flex justify-center ga-4 py-10">
    <v-btn v-tooltip>
      From activator
    </v-btn>

    <v-btn v-tooltip="'Custom text'">
      From value
    </v-btn>

    <v-btn v-tooltip="{ text: 'Custom text' }">
      From props
    </v-btn>
  </div>
</template>

```
