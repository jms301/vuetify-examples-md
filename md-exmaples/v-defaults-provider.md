# Vuetify component v-defaults-provider - usage

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
      <v-defaults-provider
        :defaults="{
          VBtn: !button ? {} : {
            color: 'primary',
            size: 'large',
            variant: 'tonal',
          },
        }"
      >
        <v-btn>Button</v-btn>
      </v-defaults-provider>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="button" label="Use v-btn defaults"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-defaults-provider'
  const model = ref('default')
  const button = ref(false)
  const options = []
  const props = computed(() => {
    return {
      defaults: button.value ? {
        VBtn: {
          color: 'primary',
          size: 'large',
          variant: 'tonal',
        },
      } : undefined,
    }
  })

  const slots = computed(() => {
    return `
  <v-btn>Button</v-btn>
`
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-defaults-provider - prop defaults

Example code

```vue
<template>
  <div>
    <v-card class="ma-10" subtitle="Subtitle" title="Title"></v-card>
    <v-defaults-provider :defaults="defaults">
      <v-card class="ma-10" subtitle="Subtitle" title="Title"></v-card>
    </v-defaults-provider>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const defaults = ref({
    global: {
      elevation: 10,
    },
    VCard: {
      color: 'secondary',
    },
  })
</script>

<script>
  export default {
    data: () => ({
      defaults: {
        global: {
          elevation: 10,
        },
        VCard: {
          color: 'secondary',
        },
      },
    }),
  }
</script>

```
