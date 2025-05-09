# Vuetify component v-tooltip - usage

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
      <v-tooltip v-bind="props">
        <template v-slot:activator="{ props: activatorProps }">
          <v-btn v-bind="activatorProps">Hover Over Me</v-btn>
        </template>

        {{ text }}
      </v-tooltip>
    </div>

    <template v-slot:configuration>
      <v-text-field v-model="text" label="Text"></v-text-field>

      <v-checkbox v-model="active" label="Always show"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-tooltip'
  const model = ref('default')
  const text = ref('Tooltip')
  const active = ref()
  const options = []
  const props = computed(() => {
    const props = {
      text: text.value || undefined,
    }

    if (active.value) {
      props['model-value'] = true
      props['onUpdate:model-value'] = true
    }

    return props
  })

  const slots = computed(() => {
    return `
  <template v-slot:activator="{ props }">
    <v-btn v-bind="props">Hover Over Me</v-btn>
  </template>
`
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-tooltip - prop color

Example code

```vue
<template>
  <div class="text-center d-flex align-center justify-space-around">
    <v-tooltip color="primary" location="bottom">
      <template v-slot:activator="{ props }">
        <v-btn
          color="primary"
          v-bind="props"
        >
          primary
        </v-btn>
      </template>
      <span>Primary tooltip</span>
    </v-tooltip>

    <v-tooltip color="success" location="bottom">
      <template v-slot:activator="{ props }">
        <v-btn
          color="success"
          v-bind="props"
        >
          success
        </v-btn>
      </template>
      <span>Success tooltip</span>
    </v-tooltip>

    <v-tooltip color="warning" location="bottom">
      <template v-slot:activator="{ props }">
        <v-btn
          color="warning"
          v-bind="props"
        >
          warning
        </v-btn>
      </template>
      <span>Warning tooltip</span>
    </v-tooltip>

    <v-tooltip color="error" location="bottom">
      <template v-slot:activator="{ props }">
        <v-btn
          color="error"
          v-bind="props"
        >
          error
        </v-btn>
      </template>
      <span>Error tooltip</span>
    </v-tooltip>
  </div>
</template>

```

# Vuetify component v-tooltip - prop location

Example code

```vue
<template>
  <div class="d-flex justify-space-around">
    <v-btn>
      Start
      <v-tooltip
        activator="parent"
        location="start"
      >Tooltip</v-tooltip>
    </v-btn>

    <v-btn>
      End
      <v-tooltip
        activator="parent"
        location="end"
      >Tooltip</v-tooltip>
    </v-btn>

    <v-btn>
      Top
      <v-tooltip
        activator="parent"
        location="top"
      >Tooltip</v-tooltip>
    </v-btn>

    <v-btn>
      Bottom
      <v-tooltip
        activator="parent"
        location="bottom"
      >Tooltip</v-tooltip>
    </v-btn>
  </div>
</template>

```

# Vuetify component v-tooltip - prop visibility

Example code

```vue
<template>
  <v-container
    class="text-center"
    fluid
  >
    <v-row
      class="flex"
      justify="space-between"
    >
      <v-col cols="12">
        <v-btn @click="show = !show">
          toggle
        </v-btn>
      </v-col>

      <v-col
        class="mt-12"
        cols="12"
      >
        <v-tooltip
          v-model="show"
          location="top"
        >
          <template v-slot:activator="{ props }">
            <v-btn
              icon
              v-bind="props"
            >
              <v-icon color="grey-lighten-1">
                mdi-cart
              </v-icon>
            </v-btn>
          </template>
          <span>Programmatic tooltip</span>
        </v-tooltip>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const show = ref(false)
</script>

<script>
  export default {
    data () {
      return {
        show: false,
      }
    },
  }
</script>

```
