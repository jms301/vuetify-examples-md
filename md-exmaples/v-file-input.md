# Vuetify component v-file-input - usage

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
      <v-file-input v-bind="props"></v-file-input>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="clear" label="Clearable"></v-checkbox>

      <v-checkbox v-model="disabled" label="Disabled"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-file-input'
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
      label: 'File input',
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

# Vuetify component v-file-input - prop accept

Example code

```vue
<template>
  <v-file-input
    accept="image/*"
    label="File input"
  ></v-file-input>
</template>

```

# Vuetify component v-file-input - prop dense

Example code

```vue
<template>
  <v-file-input
    density="compact"
    label="File input"
  ></v-file-input>
</template>

```

# Vuetify component v-file-input - prop validation

Example code

```vue
<template>
  <v-file-input
    :rules="rules"
    accept="image/png, image/jpeg, image/bmp"
    label="Photos"
    placeholder="Upload your photos"
    prepend-icon="mdi-camera"
    multiple
  ></v-file-input>
</template>

<script setup>
  const maxSize = 5000000 // 5 MB
  const errorMessage = 'Total image size should be less than 5 MB!'

  const rules = [
    value => {
      // Multiple files
      if (value && Array.isArray(value)) {
        const totalSize = value.reduce((acc, current) => acc + current.size, 0)
        return totalSize < maxSize || errorMessage
      }

      // Single file (if multiple is undefined or set to false)
      return !value || value.size < maxSize || errorMessage
    },
  ]
</script>

```

# Vuetify component v-file-input - prop counter

Example code

```vue
<template>
  <v-file-input
    label="File input"
    counter
    multiple
    show-size
  ></v-file-input>
</template>

```

# Vuetify component v-file-input - prop multiple

Example code

```vue
<template>
  <v-file-input
    label="File input"
    multiple
  ></v-file-input>
</template>

```

# Vuetify component v-file-input - slot selection

Example code

```vue
<template>
  <v-file-input
    v-model="files"
    label="File input"
    placeholder="Upload your documents"
    prepend-icon="mdi-paperclip"
    multiple
  >
    <template v-slot:selection="{ fileNames }">
      <template v-for="fileName in fileNames" :key="fileName">
        <v-chip
          class="me-2"
          color="primary"
          size="small"
          label
        >
          {{ fileName }}
        </v-chip>
      </template>
    </template>
  </v-file-input>
</template>

<script setup>
  import { ref } from 'vue'

  const files = ref([])
</script>

<script>
  export default {
    data: () => ({
      files: [],
    }),
  }
</script>

```

# Vuetify component v-file-input - prop prepend icon

Example code

```vue
<template>
  <v-file-input
    label="File input"
    prepend-icon="mdi-camera"
    variant="filled"
  ></v-file-input>
</template>

```

# Vuetify component v-file-input - misc complex selection

Example code

```vue
<template>
  <v-file-input
    v-model="files"
    :show-size="1000"
    color="deep-purple-accent-4"
    label="File input"
    placeholder="Select your files"
    prepend-icon="mdi-paperclip"
    variant="outlined"
    counter
    multiple
  >
    <template v-slot:selection="{ fileNames }">
      <template v-for="(fileName, index) in fileNames" :key="fileName">
        <v-chip
          v-if="index < 2"
          class="me-2"
          color="deep-purple-accent-4"
          size="small"
          label
        >
          {{ fileName }}
        </v-chip>

        <span
          v-else-if="index === 2"
          class="text-overline text-grey-darken-3 mx-2"
        >
          +{{ files.length - 2 }} File(s)
        </span>
      </template>
    </template>
  </v-file-input>
</template>

<script setup>
  import { ref } from 'vue'

  const files = ref([])
</script>

<script>
  export default {
    data: () => ({
      files: [],
    }),
  }
</script>

```

# Vuetify component v-file-input - prop show size

Example code

```vue
<template>
  <v-file-input
    label="File input"
    show-size
  ></v-file-input>
</template>

```

# Vuetify component v-file-input - prop chips

Example code

```vue
<template>
  <div>
    <v-file-input
      label="File input w/ chips"
      chips
      multiple
    ></v-file-input>
  </div>
</template>

```
