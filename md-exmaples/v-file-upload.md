# Vuetify component v-file-upload - usage

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
      <v-file-upload v-bind="props"></v-file-upload>
    </div>

    <template v-slot:configuration>
      <v-text-field v-model="title" label="Title"></v-text-field>

      <v-checkbox v-model="disabled" label="Disabled"></v-checkbox>

      <v-checkbox v-model="clear" label="Clearable"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-file-upload'
  const model = ref('default')
  const options = ['comfortable', 'compact']
  const clear = ref(false)
  const counter = ref(false)
  const disabled = ref(false)
  const title = ref()
  const props = computed(() => {
    return {
      clearable: clear.value || undefined,
      counter: counter.value || undefined,
      disabled: disabled.value || undefined,
      density: model.value,
      title: title.value || undefined,
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

# Vuetify component v-file-upload - prop scrim

Example code

```vue
<template>
  <v-file-upload scrim="primary"></v-file-upload>
</template>

```

# Vuetify component v-file-upload - prop density

Example code

```vue
<template>
  <div class="text-center pa-2 mb-2">
    <v-btn-toggle v-model="density" density="comfortable" border divided rounded>
      <v-btn value="default">Default</v-btn>

      <v-btn value="comfortable">Comfortable</v-btn>

      <v-btn value="compact">Compact</v-btn>
    </v-btn-toggle>
  </div>

  <v-file-upload :density="density"></v-file-upload>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const density = shallowRef('default')
</script>

```

# Vuetify component v-file-upload - prop content

Example code

```vue
<template>
  <v-file-upload
    browse-text="Local Filesystem"
    divider-text="or choose locally"
    icon="mdi-upload"
    title="Drag and Drop Here"
  ></v-file-upload>
</template>

```

# Vuetify component v-file-upload - prop disabled

Example code

```vue
<template>
  <v-file-upload disabled></v-file-upload>
</template>

```

# Vuetify component v-file-upload - slot item

Example code

```vue
<template>
  <v-file-upload
    v-model="model"
    clearable
    multiple
    show-size
  >
    <template v-slot:item="{ props: itemProps }">
      <v-file-upload-item v-bind="itemProps" lines="one" nav>
        <template v-slot:prepend>
          <v-avatar size="32" rounded></v-avatar>
        </template>

        <template v-slot:clear="{ props: clearProps }">
          <v-btn color="primary" v-bind="clearProps"></v-btn>
        </template>
      </v-file-upload-item>
    </template>
  </v-file-upload>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const model = shallowRef(null)
</script>

```
