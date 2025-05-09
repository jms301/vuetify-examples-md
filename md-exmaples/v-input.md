# Vuetify component v-input - usage

Example code

```vue
<template>
  <v-container
    id="input-usage"
    fluid
  >
    <v-row>
      <v-col cols="12">
        <v-input
          :messages="['Messages']"
          append-icon="mdi-close"
          prepend-icon="mdi-phone"
        >
          Default Slot
        </v-input>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-input - prop hint

Example code

```vue
<template>
  <v-switch
    v-model="showMessages"
    label="Show messages"
    hide-details
  ></v-switch>
  <v-input
    :messages="messages"
    hint="I am hint"
    persistent-hint
  >
    Input
  </v-input>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const showMessages = ref(false)
  const messages = computed(() => {
    return showMessages.value ? ['Message'] : undefined
  })
</script>

<script>
  export default {
    data: () => ({
      showMessages: false,
    }),

    computed: {
      messages () {
        return this.showMessages ? ['Message'] : undefined
      },
    },
  }
</script>

```

# Vuetify component v-input - prop loading

Example code

```vue
<template>
  <v-text-field
    color="success"
    disabled
    loading
  ></v-text-field>
</template>

```

# Vuetify component v-input - slot append and prepend

Example code

```vue
<template>
  <v-text-field>
    <template v-slot:append>
      <v-icon color="red">
        mdi-plus
      </v-icon>
    </template>
    <template v-slot:prepend>
      <v-icon color="green">
        mdi-minus
      </v-icon>
    </template>
  </v-text-field>
</template>

```

# Vuetify component v-input - prop rules

Example code

```vue
<template>
  <v-text-field :rules="rules"></v-text-field>
</template>

<script setup>
  const rules = [
    value => !!value || 'Required.',
    value => (value || '').length <= 20 || 'Max 20 characters',
    value => {
      const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      return pattern.test(value) || 'Invalid e-mail.'
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      rules: [
        value => !!value || 'Required.',
        value => (value || '').length <= 20 || 'Max 20 characters',
        value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'Invalid e-mail.'
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-input - event slot clicks

Example code

```vue
<template>
  <v-container
    id="input-usage"
    fluid
  >
    <v-row>
      <v-col cols="12">
        <v-input
          :messages="['Messages']"
          append-icon="mdi-close"
          prepend-icon="mdi-phone"
          @click:append="appendIconCallback"
          @click:prepend="prependIconCallback"
        >
          Default Slot
        </v-input>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  function appendIconCallback () {
    alert('click:append')
  }
  function prependIconCallback () {
    alert('click:prepend')
  }
</script>

<script>
  export default {
    methods: {
      appendIconCallback () {
        alert('click:append')
      },
      prependIconCallback () {
        alert('click:prepend')
      },
    },
  }
</script>

<style>
  #input-usage .v-input__prepend-outer,
  #input-usage .v-input__append-outer,
  #input-usage .v-input__slot,
  #input-usage .v-messages {
    border: 1px dashed rgba(0,0,0, .4);
  }
</style>

```

# Vuetify component v-input - prop error count

Example code

```vue
<template>
  <v-input
    :error-messages="['Fatal error', 'Another error']"
    max-errors="2"
    disabled
    error
  >
    Input
  </v-input>
</template>

```

# Vuetify component v-input - prop error

Example code

```vue
<template>
  <v-input
    :error-messages="['Fatal error']"
    disabled
    error
  >
    Input
  </v-input>
</template>

```

# Vuetify component v-input - prop hide details

Example code

```vue
<template>
  <div>
    <v-text-field
      :rules="rules"
      hide-details="auto"
      label="Main input"
    ></v-text-field>
    <v-text-field label="Another input"></v-text-field>
  </div>
</template>

<script setup>
  const rules = [
    value => !!value || 'Required.',
    value => (value && value.length >= 3) || 'Min 3 characters',
  ]
</script>

<script>
  export default {
    data: () => ({
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
    }),
  }
</script>

```
