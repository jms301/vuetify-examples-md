# Vuetify component v-snackbar - usage

Example code

```vue
<template>
  <div class="text-center ma-2">
    <v-btn
      @click="snackbar = true"
    >
      Open Snackbar
    </v-btn>
    <v-snackbar
      v-model="snackbar"
    >
      {{ text }}

      <template v-slot:actions>
        <v-btn
          color="pink"
          variant="text"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
  export default {
    data: () => ({
      snackbar: false,
      text: `Hello, I'm a snackbar`,
    }),
  }
</script>

```

# Vuetify component v-snackbar - prop multi line

Example code

```vue
<template>
  <div class="text-center">
    <v-btn
      color="red-darken-2"
      @click="snackbar = true"
    >
      Open Snackbar
    </v-btn>

    <v-snackbar
      v-model="snackbar"
      multi-line
    >
      {{ text }}

      <template v-slot:actions>
        <v-btn
          color="red"
          variant="text"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const snackbar = ref(false)

  const text = `I am a multi-line snackbar.\nI can have more than one line. This is another line that is quite long.`
</script>

<script>
  export default {
    data: () => ({
      snackbar: false,
      text: `I am a multi-line snackbar.\nI can have more than one line. This is another line that is quite long.`,
    }),
  }
</script>

```

# Vuetify component v-snackbar - prop timeout

Example code

```vue
<template>
  <div class="text-center">
    <v-btn
      color="orange-darken-2"
      @click="snackbar = true"
    >
      Open Snackbar
    </v-btn>

    <v-snackbar
      v-model="snackbar"
      :timeout="timeout"
    >
      {{ text }}

      <template v-slot:actions>
        <v-btn
          color="blue"
          variant="text"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const snackbar = ref(false)
  const text = ref('My timeout is set to 2000.')
  const timeout = ref(2000)
</script>

<script>
  export default {
    data: () => ({
      snackbar: false,
      text: 'My timeout is set to 2000.',
      timeout: 2000,
    }),
  }
</script>

```

# Vuetify component v-snackbar - prop vertical

Example code

```vue
<template>
  <div class="text-center">
    <v-btn
      color="indigo"
      @click="snackbar = true"
    >
      Open Snackbar
    </v-btn>

    <v-snackbar
      v-model="snackbar"
      vertical
    >
      <div class="text-subtitle-1 pb-2">This is a snackbar message</div>

      <p>This is a longer paragraph explaining something</p>

      <template v-slot:actions>
        <v-btn
          color="indigo"
          variant="text"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const snackbar = ref(false)
</script>

<script>
  export default {
    data: () => ({
      snackbar: false,
    }),
  }
</script>

```

# Vuetify component v-snackbar - prop variants

Example code

```vue
<template>
  <v-sheet
    class="d-flex flex-column"
  >
    <v-snackbar
      :timeout="2000"
    >
      <template v-slot:activator="{ props }">
        <v-btn class="ma-2" v-bind="props">open</v-btn>
      </template>

      Lorem ipsum dolor sit amet consectetur.
    </v-snackbar>

    <v-snackbar
      :timeout="2000"
      color="blue-grey"
      rounded="pill"
    >
      <template v-slot:activator="{ props }">
        <v-btn class="ma-2" color="blue-grey" rounded="pill" v-bind="props">open</v-btn>
      </template>

      Snackbar with <strong>rounded="pill"</strong>.
    </v-snackbar>

    <v-snackbar
      :timeout="2000"
      class="elevation-24"
      color="deep-purple-accent-4"
    >
      <template v-slot:activator="{ props }">
        <v-btn class="ma-2" color="deep-purple-accent-4" v-bind="props">open</v-btn>
      </template>

      Snackbar with <strong>elevation="24"</strong>.
    </v-snackbar>

    <v-snackbar
      :timeout="2000"
      color="primary"
      variant="tonal"
    >
      <template v-slot:activator="{ props }">
        <v-btn class="ma-2" color="primary" variant="tonal" v-bind="props">open</v-btn>
      </template>

      Snackbar with <strong>tonal</strong> variant.
    </v-snackbar>

    <v-snackbar
      :timeout="2000"
      color="success"
      variant="outlined"
    >
      <template v-slot:activator="{ props }">
        <v-btn class="ma-2" color="success" variant="outlined" v-bind="props">open</v-btn>
      </template>

      Snackbar with <strong>outlined</strong> variant.
    </v-snackbar>
  </v-sheet>
</template>

```
