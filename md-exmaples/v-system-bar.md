# Vuetify component v-system-bar - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <v-layout
      class="elevation-2 rounded mx-auto bg-white"
      style="max-width: 448px; height: 150px"
    >
      <v-system-bar v-bind="props">
        <v-icon icon="mdi-wifi-strength-4"></v-icon>
        <v-icon class="ms-2" icon="mdi-signal"></v-icon>
        <v-icon class="ms-2" icon="mdi-battery"></v-icon>

        <span class="ms-2">3:13PM</span>
      </v-system-bar>

      <v-main></v-main>
    </v-layout>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-system-bar'
  const model = ref('default')
  const options = ['window']

  const props = computed(() => {
    return {
      window: model.value === 'window' || undefined,
    }
  })
  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>
  <v-icon icon="mdi-wifi-strength-4"></v-icon>
  <v-icon icon="mdi-signal" class="ms-2"></v-icon>
  <v-icon icon="mdi-battery" class="ms-2"></v-icon>

  <span class="ms-2">3:13PM</span>
</${name}>`
  })
</script>

```

# Vuetify component v-system-bar - prop color

Example code

```vue
<template>
  <div>
    <v-layout style="height: 50px">
      <v-system-bar color="primary">
        <v-icon class="ms-2" icon="mdi-wifi-strength-4"></v-icon>

        <v-icon class="ms-2" icon="mdi-signal-cellular-outline"></v-icon>

        <v-icon class="ms-2" icon="mdi-battery"></v-icon>

        <span class="ms-2">08:30</span>
      </v-system-bar>
    </v-layout>

    <v-layout style="height: 50px">
      <v-system-bar color="red-lighten-2">
        <v-icon class="ms-2" icon="mdi-wifi-strength-2"></v-icon>

        <v-icon class="ms-2" icon="mdi-signal-cellular-outline"></v-icon>

        <v-icon class="ms-2" icon="mdi-battery"></v-icon>

        <span class="ms-2">18:30</span>
      </v-system-bar>
    </v-layout>

    <v-layout style="height: 50px">
      <v-system-bar color="indigo-darken-2">
        <v-icon class="ms-2" icon="mdi-wifi-strength-3"></v-icon>

        <v-icon class="ms-2" icon="mdi-signal-cellular-outline"></v-icon>

        <v-icon class="ms-2" icon="mdi-battery"></v-icon>

        <span class="ms-2">13:24</span>
      </v-system-bar>
    </v-layout>
  </div>
</template>

```

# Vuetify component v-system-bar - prop window

Example code

```vue
<template>
  <v-layout style="height: 50px">
    <v-system-bar window>
      <v-icon class="me-2" icon="mdi-message"></v-icon>

      <span>10 unread messages</span>

      <v-spacer></v-spacer>

      <v-btn icon="mdi-minus" variant="text"></v-btn>

      <v-btn class="ms-2" icon="mdi-checkbox-blank-outline" variant="text"></v-btn>

      <v-btn class="ms-2" icon="mdi-close" variant="text"></v-btn>
    </v-system-bar>
  </v-layout>
</template>

```
