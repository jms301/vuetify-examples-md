# Vuetify component v-overflow-btn - usage

Example code

```vue
<template>
  <v-container id="dropdown-playground">
    <v-overflow-btn
      :items="dropdownFont"
      hint="I'm a hint"
      label="Overflow Btn"
      target="#dropdown-playground"
      v-bind="$attrs"
    ></v-overflow-btn>
  </v-container>
</template>

<script>
  export default {
    name: 'Usage',

    inheritAttrs: false,

    data: () => ({
      dropdownFont: [
        { text: 'Arial', callback: () => {} },
        { text: 'Calibri', callback: () => {} },
        { text: 'Courier', callback: () => {} },
        { text: 'Verdana', callback: () => {} },
      ],
      defaults: {
        dense: false,
        disabled: false,
        editable: false,
        filled: false,
        loading: false,
        overflow: false,
        'persistent-hint': false,
        readonly: false,
        reverse: false,
        segmented: false,
      },
      options: {
        booleans: [
          'dense',
          'disabled',
          'filled',
          'loading',
          'persistent-hint',
          'readonly',
          'reverse',
        ],
      },
      tabs: ['editable', 'overflow', 'segmented'],
    }),
  }
</script>

```

# Vuetify component v-overflow-btn - prop dense

Example code

```vue
<template>
  <v-container>
    <v-overflow-btn
      :items="items"
      class="my-2"
      label="Overflow Btn - Dense"
      dense
    ></v-overflow-btn>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref(['Arial', 'Calibri', 'Courier', 'Verdana'])
</script>

<script>
  export default {
    data: () => ({
      items: ['Arial', 'Calibri', 'Courier', 'Verdana'],
    }),
  }
</script>

```

# Vuetify component v-overflow-btn - prop hint

Example code

```vue
<template>
  <v-container id="dropdown-example-1">
    <v-overflow-btn
      :items="dropdownFont"
      class="my-2"
      hint="Select font"
      label="Overflow Btn w/ hint"
      menu-props="top"
      target="#dropdown-example-1"
    ></v-overflow-btn>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const dropdownFont = ref(['Arial', 'Calibri', 'Courier', 'Verdana'])
</script>

<script>
  export default {
    data: () => ({
      dropdownFont: ['Arial', 'Calibri', 'Courier', 'Verdana'],
    }),
  }
</script>

```

# Vuetify component v-overflow-btn - prop loading

Example code

```vue
<template>
  <v-container id="dropdown-example-1">
    <v-overflow-btn
      :items="dropdownFont"
      class="my-2"
      label="Overflow Btn w/ loading"
      target="#dropdown-example-1"
      loading
    ></v-overflow-btn>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const dropdownFont = ref(['Arial', 'Calibri', 'Courier', 'Verdana'])
</script>

<script>
  export default {
    data: () => ({
      dropdownFont: ['Arial', 'Calibri', 'Courier', 'Verdana'],
    }),
  }
</script>

```

# Vuetify component v-overflow-btn - prop counter

Example code

```vue
<template>
  <v-container id="dropdown-example-3">
    <v-overflow-btn
      :items="dropdownEdit"
      class="my-2"
      item-value="text"
      label="Overflow Btn w/ counter"
      counter
    ></v-overflow-btn>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const dropdownEdit = ref([
    { text: '100%' },
    { text: '75%' },
    { text: '50%' },
    { text: '25%' },
    { text: '0%' },
  ])
</script>

<script>
  export default {
    data: () => ({
      dropdownEdit: [
        { text: '100%' },
        { text: '75%' },
        { text: '50%' },
        { text: '25%' },
        { text: '0%' },
      ],
    }),
  }
</script>

```

# Vuetify component v-overflow-btn - prop editable

Example code

```vue
<template>
  <v-container id="dropdown-example-3">
    <v-overflow-btn
      :items="dropdownEdit"
      class="my-2"
      item-value="text"
      label="Overflow Btn w/ editable"
      editable
    ></v-overflow-btn>
  </v-container>
</template>

<script setup>
  const dropdownEdit = [
    { text: '100%' },
    { text: '75%' },
    { text: '50%' },
    { text: '25%' },
    { text: '0%' },
  ]
</script>

<script>
  export default {
    data: () => ({
      dropdownEdit: [
        { text: '100%' },
        { text: '75%' },
        { text: '50%' },
        { text: '25%' },
        { text: '0%' },
      ],
    }),
  }
</script>

```

# Vuetify component v-overflow-btn - prop filled

Example code

```vue
<template>
  <v-container id="dropdown-example-1">
    <v-overflow-btn
      :items="dropdownFont"
      class="my-2"
      label="Overflow Btn - filled"
      target="#dropdown-example-1"
      filled
    ></v-overflow-btn>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const dropdownFont = ref(['Arial', 'Calibri', 'Courier', 'Verdana'])
</script>

<script>
  export default {
    data: () => ({
      dropdownFont: ['Arial', 'Calibri', 'Courier', 'Verdana'],
    }),
  }
</script>

```

# Vuetify component v-overflow-btn - prop menu props

Example code

```vue
<template>
  <v-container id="dropdown-example-1">
    <v-overflow-btn
      :items="dropdownFont"
      class="my-2"
      label="Overflow Btn w/ menu-props"
      menu-props="top"
      target="#dropdown-example-1"
    ></v-overflow-btn>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const dropdownFont = ref(['Arial', 'Calibri', 'Courier', 'Verdana'])
</script>

<script>
  export default {
    data: () => ({
      dropdownFont: ['Arial', 'Calibri', 'Courier', 'Verdana'],
    }),
  }
</script>

```

# Vuetify component v-overflow-btn - prop readonly

Example code

```vue
<template>
  <v-container id="dropdown-example-1">
    <v-overflow-btn
      :items="dropdownFont"
      class="my-2"
      label="Overflow Btn w/ readonly"
      target="#dropdown-example-1"
      readonly
    ></v-overflow-btn>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const dropdownFont = ref(['Arial', 'Calibri', 'Courier', 'Verdana'])
</script>

<script>
  export default {
    data: () => ({
      dropdownFont: ['Arial', 'Calibri', 'Courier', 'Verdana'],
    }),
  }
</script>

```

# Vuetify component v-overflow-btn - prop disabled

Example code

```vue
<template>
  <v-container id="dropdown-example-1">
    <v-overflow-btn
      :items="dropdownFont"
      class="my-2"
      label="Overflow Btn w/ disabled"
      target="#dropdown-example-1"
      disabled
    ></v-overflow-btn>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const dropdownFont = ref(['Arial', 'Calibri', 'Courier', 'Verdana'])
</script>

<script>
  export default {
    data: () => ({
      dropdownFont: ['Arial', 'Calibri', 'Courier', 'Verdana'],
    }),
  }
</script>

```

# Vuetify component v-overflow-btn - prop segmented

Example code

```vue
<template>
  <v-container id="dropdown-example-2">
    <v-overflow-btn
      :items="dropdownIcon"
      class="my-2"
      label="Overflow Btn w/ segmented"
      target="#dropdown-example-2"
      segmented
    ></v-overflow-btn>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const dropdownIcon = ref([
    { text: 'list', callback: () => console.log('list') },
    { text: 'favorite', callback: () => console.log('favorite') },
    { text: 'delete', callback: () => console.log('delete') },
  ])
</script>

<script>
  export default {
    data: () => ({
      dropdownIcon: [
        { text: 'list', callback: () => console.log('list') },
        { text: 'favorite', callback: () => console.log('favorite') },
        { text: 'delete', callback: () => console.log('delete') },
      ],
    }),
  }
</script>

```
