# Vuetify component v-textarea - usage

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
      <v-textarea v-bind="props" v-model="field" hide-details></v-textarea>
    </div>

    <template v-slot:configuration>
      <v-text-field v-model="label" label="Label"></v-text-field>

      <v-checkbox v-model="prepend" label="Prepend icon"></v-checkbox>

      <v-checkbox v-model="clearable" label="Clearable"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-textarea'
  const model = ref('default')
  const clearable = ref(false)
  const field = ref()
  const label = ref('Label')
  const prepend = ref(false)
  const options = ['outlined', 'underlined', 'solo', 'solo-filled', 'solo-inverted']
  const props = computed(() => {
    return {
      clearable: clearable.value || undefined,
      label: label.value,
      'prepend-icon': prepend.value ? '$vuetify' : undefined,
      variant: model.value === 'default' ? undefined : model.value,
    }
  })

  const slots = computed(() => {
    return ``
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })

  watch(clearable, () => {
    if (!field.value) field.value = 'Hover to Clear me'
  })
</script>

```

# Vuetify component v-textarea - prop auto grow

Example code

```vue
<template>
  <v-container fluid>
    <v-textarea
      label="Label"
      model-value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
      name="input-7-1"
      variant="filled"
      auto-grow
    ></v-textarea>
  </v-container>
</template>

```

# Vuetify component v-textarea - prop clearable

Example code

```vue
<template>
  <v-container fluid>
    <v-textarea
      clear-icon="mdi-close-circle"
      label="Text"
      model-value="This is clearable text."
      clearable
    ></v-textarea>
  </v-container>
</template>

```

# Vuetify component v-textarea - prop counter

Example code

```vue
<template>
  <v-container fluid>
    <v-textarea
      :model-value="value"
      :rules="rules"
      label="Text"
      counter
    ></v-textarea>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const rules = [v => v.length <= 25 || 'Max 25 characters']

  const value = ref('Hello!')
</script>

<script>
  export default {
    data: () => ({
      rules: [v => v.length <= 25 || 'Max 25 characters'],
      value: 'Hello!',
    }),
  }
</script>

```

# Vuetify component v-textarea - prop no resize

Example code

```vue
<template>
  <v-container fluid>
    <v-textarea
      :model-value="value"
      label="Text"
      rows="1"
      no-resize
    ></v-textarea>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.')
</script>

<script>
  export default {
    data: () => ({
      value: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    }),
  }
</script>

```

# Vuetify component v-textarea - prop browser autocomplete

Example code

```vue
<template>
  <v-container fluid>
    <v-textarea
      autocomplete="email"
      label="Email"
    ></v-textarea>
  </v-container>
</template>

```

# Vuetify component v-textarea - prop icons

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col
        cols="12"
        sm="6"
      >
        <v-textarea
          class="mx-2"
          label="prepend-icon"
          prepend-icon="mdi-comment"
          rows="1"
        ></v-textarea>
      </v-col>
      <v-col
        cols="12"
        sm="6"
      >
        <v-textarea
          append-icon="mdi-comment"
          class="mx-2"
          label="append-icon"
          rows="1"
        ></v-textarea>
      </v-col>
      <v-col
        cols="12"
        sm="6"
      >
        <v-textarea
          class="mx-2"
          label="prepend-inner-icon"
          prepend-inner-icon="mdi-comment"
          rows="1"
        ></v-textarea>
      </v-col>
      <v-col
        cols="12"
        sm="6"
      >
        <v-textarea
          append-inner-icon="mdi-comment"
          class="mx-2"
          label="append-inner-icon"
          rows="1"
        ></v-textarea>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-textarea - misc signup form

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    style="max-width: 500px;"
  >
    <v-toolbar
      color="deep-purple-accent-4"
      cards
      dark
      flat
    >
      <v-btn icon>
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-card-title class="text-h6 font-weight-regular">
        Sign up
      </v-card-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>
    <v-form
      ref="form"
      v-model="isValid"
      class="pa-4 pt-6"
    >
      <v-text-field
        v-model="password"
        :rules="[rules.password, rules.length(6)]"
        color="deep-purple"
        counter="6"
        label="Password"
        style="min-height: 96px"
        type="password"
        variant="filled"
      ></v-text-field>
      <v-text-field
        v-model="phone"
        color="deep-purple"
        label="Phone number"
        variant="filled"
      ></v-text-field>
      <v-text-field
        v-model="email"
        :rules="[rules.email]"
        color="deep-purple"
        label="Email address"
        type="email"
        variant="filled"
      ></v-text-field>
      <v-textarea
        v-model="bio"
        color="deep-purple"
        label="Bio"
        rows="1"
        variant="filled"
        auto-grow
      ></v-textarea>
      <v-checkbox
        v-model="agreement"
        :rules="[rules.required]"
        color="deep-purple"
      >
        <template v-slot:label>
          I agree to the&nbsp;
          <a
            href="#"
            @click.stop.prevent="dialog = true"
          >Terms of Service</a>
          &nbsp;and&nbsp;
          <a
            href="#"
            @click.stop.prevent="dialog = true"
          >Privacy Policy</a>*
        </template>
      </v-checkbox>
    </v-form>
    <v-divider></v-divider>
    <v-card-actions>
      <v-btn
        variant="text"
        @click="form.reset()"
      >
        Clear
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        :disabled="!isValid"
        :loading="isLoading"
        color="deep-purple-accent-4"
      >
        Submit
      </v-btn>
    </v-card-actions>
    <v-dialog
      v-model="dialog"
      max-width="400"
      persistent
    >
      <v-card>
        <v-card-title class="text-h5 bg-grey-lighten-3">
          Legal
        </v-card-title>
        <v-card-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            variant="text"
            @click="agreement = false, dialog = false"
          >
            No
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            color="deep-purple"
            variant="tonal"
            @click="agreement = true, dialog = false"
          >
            Yes
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const rules = {
    email: v => !!(v || '').match(/@/) || 'Please enter a valid email',
    length: len => v => (v || '').length >= len || `Invalid character length, required ${len}`,
    password: v => !!(v || '').match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$/) || 'Password must contain an upper case letter, a numeric character, and a special character',
    required: v => !!v || 'This field is required',
  }

  const form = ref()

  const agreement = ref(false)
  const bio = ref('Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts')
  const dialog = ref(false)
  const email = ref()
  const isValid = ref(false)
  const isLoading = ref(false)
  const password = ref()
  const phone = ref()
</script>

<script>
  export default {
    data: () => ({
      agreement: false,
      bio: 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts',
      dialog: false,
      email: undefined,
      isValid: false,
      isLoading: false,
      password: undefined,
      phone: undefined,
      rules: {
        email: v => !!(v || '').match(/@/) || 'Please enter a valid email',
        length: len => v => (v || '').length >= len || `Invalid character length, required ${len}`,
        password: v => !!(v || '').match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$/) ||
          'Password must contain an upper case letter, a numeric character, and a special character',
        required: v => !!v || 'This field is required',
      },
    }),
  }
</script>

```

# Vuetify component v-textarea - prop background color

Example code

```vue
<template>
  <v-container>
    <v-textarea
      bg-color="light-blue"
      color="black"
      label="Label"
    ></v-textarea>

    <v-textarea
      bg-color="grey-lighten-2"
      color="cyan"
      label="Label"
    ></v-textarea>

    <v-textarea
      bg-color="amber-lighten-4"
      color="orange orange-darken-4"
      label="Label"
    ></v-textarea>
  </v-container>
</template>

```

# Vuetify component v-textarea - prop rows

Example code

```vue
<template>
  <v-container fluid>
    <v-row>
      <v-col
        cols="12"
        sm="6"
      >
        <v-textarea
          label="One row"
          row-height="15"
          rows="1"
          variant="outlined"
          auto-grow
        ></v-textarea>
      </v-col>
      <v-col
        cols="12"
        sm="6"
      >
        <v-textarea
          label="Two rows"
          row-height="20"
          rows="2"
          variant="filled"
          auto-grow
        ></v-textarea>
      </v-col>
      <v-col
        cols="12"
        sm="6"
      >
        <v-textarea
          label="Three rows"
          row-height="25"
          rows="3"
          variant="outlined"
          auto-grow
        ></v-textarea>
      </v-col>
      <v-col
        cols="12"
        sm="6"
      >
        <v-textarea
          label="Four rows"
          row-height="30"
          rows="4"
          variant="filled"
          auto-grow
        ></v-textarea>
      </v-col>
    </v-row>
  </v-container>
</template>

```
