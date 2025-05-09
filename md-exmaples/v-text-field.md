# Vuetify component v-text-field - usage

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
      <v-text-field v-bind="props" v-model="field"></v-text-field>
    </div>

    <template v-slot:configuration>
      <v-text-field v-model="label" label="Label"></v-text-field>

      <v-checkbox v-model="prepend" label="Prepend icon"></v-checkbox>

      <v-checkbox v-model="clearable" label="Clearable"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-text-field'
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

# Vuetify component v-text-field - prop dense

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    color="surface-light"
    max-width="400"
  >
    <v-card-text>
      <v-text-field
        :loading="loading"
        append-inner-icon="mdi-magnify"
        density="compact"
        label="Search templates"
        variant="solo"
        hide-details
        single-line
        @click:append-inner="onClick"
      ></v-text-field>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const loaded = ref(false)
  const loading = ref(false)

  function onClick () {
    loading.value = true
    setTimeout(() => {
      loading.value = false
      loaded.value = true
    }, 2000)
  }
</script>

<script>
  export default {
    data: () => ({
      loaded: false,
      loading: false,
    }),

    methods: {
      onClick () {
        this.loading = true

        setTimeout(() => {
          this.loading = false
          this.loaded = true
        }, 2000)
      },
    },
  }
</script>

```

# Vuetify component v-text-field - prop messages

Example code

```vue
<template>
  <v-responsive
    class="mx-auto"
    max-width="344"
  >
    <v-text-field
      hint="Enter your password to access this website"
      label="Password"
      type="input"
    ></v-text-field>
  </v-responsive>
</template>

```

# Vuetify component v-text-field - prop placeholder

Example code

```vue
<template>
  <v-responsive
    class="mx-auto"
    max-width="344"
  >
    <v-text-field
      hide-details="auto"
      label="Email address"
      placeholder="johndoe@gmail.com"
      type="email"
    ></v-text-field>
  </v-responsive>
</template>

```

# Vuetify component v-text-field - prop validation

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="title"
            :rules="[rules.required, rules.counter]"
            label="Title"
            maxlength="20"
            counter
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="email"
            :rules="[rules.required, rules.email]"
            label="E-mail"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
  import { ref } from 'vue'

  const title = ref('Preliminary report')
  const email = ref('')

  const rules = {
    required: value => !!value || 'Required.',
    counter: value => value.length <= 20 || 'Max 20 characters',
    email: value => {
      const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      return pattern.test(value) || 'Invalid e-mail.'
    },
  }
</script>

<script>
  export default {
    data () {
      return {
        title: 'Preliminary report',
        email: '',
        rules: {
          required: value => !!value || 'Required.',
          counter: value => value.length <= 20 || 'Max 20 characters',
          email: value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return pattern.test(value) || 'Invalid e-mail.'
          },
        },
      }
    },
  }
</script>

```

# Vuetify component v-text-field - prop variant

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          md="4"
          sm="6"
        >
          <v-text-field
            label="Regular"
            placeholder="Placeholder"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
          sm="6"
        >
          <v-text-field
            label="Solo"
            placeholder="Placeholder"
            variant="solo"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
          sm="6"
        >
          <v-text-field
            label="Filled"
            placeholder="Placeholder"
            variant="filled"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
          sm="6"
        >
          <v-text-field
            label="Outlined"
            placeholder="Placeholder"
            variant="outlined"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
          sm="6"
        >
          <v-text-field
            label="Plain"
            placeholder="Placeholder"
            variant="plain"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
          sm="6"
        >
          <v-text-field
            label="Underlined"
            placeholder="Placeholder"
            variant="underlined"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

```

# Vuetify component v-text-field - prop hint

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            hint="For example, flowers or used cars"
            label="Your product or service"
            model-value="Grocery delivery"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            hint="www.example.com/page"
            label="Your landing page"
            persistent-hint
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            hint="For example, flowers or used cars"
            label="Your product or service"
            model-value="Grocery delivery"
            variant="solo"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            hint="www.example.com/page"
            label="Your landing page"
            variant="solo"
            persistent-hint
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            hint="For example, flowers or used cars"
            label="Your product or service"
            model-value="Grocery delivery"
            variant="outlined"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            hint="www.example.com/page"
            label="Your landing page"
            variant="outlined"
            persistent-hint
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

```

# Vuetify component v-text-field - prop icon

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Prepend"
            prepend-icon="mdi-map-marker"
          ></v-text-field>

          <v-text-field
            label="Prepend inner"
            prepend-inner-icon="mdi-map-marker"
          ></v-text-field>

          <v-text-field
            append-icon="mdi-map-marker"
            label="Append"
          ></v-text-field>

          <v-text-field
            append-inner-icon="mdi-map-marker"
            label="Append inner"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Prepend"
            prepend-icon="mdi-map-marker"
            variant="solo"
          ></v-text-field>

          <v-text-field
            label="Prepend inner"
            prepend-inner-icon="mdi-map-marker"
            variant="solo"
          ></v-text-field>

          <v-text-field
            append-icon="mdi-map-marker"
            label="Append"
            variant="solo"
          ></v-text-field>

          <v-text-field
            append-inner-icon="mdi-map-marker"
            label="Append inner"
            variant="solo"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Prepend"
            prepend-icon="mdi-map-marker"
            variant="outlined"
          ></v-text-field>

          <v-text-field
            label="Prepend inner"
            prepend-inner-icon="mdi-map-marker"
            variant="outlined"
          ></v-text-field>

          <v-text-field
            append-icon="mdi-map-marker"
            label="Append"
            variant="outlined"
          ></v-text-field>

          <v-text-field
            append-inner-icon="mdi-map-marker"
            label="Append inner"
            variant="outlined"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Prepend"
            prepend-icon="mdi-map-marker"
            variant="underlined"
          ></v-text-field>

          <v-text-field
            label="Prepend inner"
            prepend-inner-icon="mdi-map-marker"
            variant="underlined"
          ></v-text-field>

          <v-text-field
            append-icon="mdi-map-marker"
            label="Append"
            variant="underlined"
          ></v-text-field>

          <v-text-field
            append-inner-icon="mdi-map-marker"
            label="Append inner"
            variant="underlined"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

```

# Vuetify component v-text-field - prop contained

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="first"
            label="First Name"
            variant="solo"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="last"
            label="Last Name"
            variant="solo"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
  import { ref } from 'vue'

  const first = ref('John')
  const last = ref('Doe')
</script>

<script>
  export default {
    data: () => ({
      first: 'John',
      last: 'Doe',
    }),
  }
</script>

```

# Vuetify component v-text-field - prop disabled and readonly

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Regular"
            model-value="John Doe"
            disabled
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Regular"
            model-value="John Doe"
            readonly
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Solo"
            model-value="John Doe"
            variant="solo"
            disabled
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Solo"
            model-value="John Doe"
            variant="solo"
            readonly
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Outlined"
            model-value="John Doe"
            variant="outlined"
            disabled
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Outlined"
            model-value="John Doe"
            variant="outlined"
            readonly
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="underlined"
            model-value="John Doe"
            variant="underlined"
            disabled
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="underlined"
            model-value="John Doe"
            variant="underlined"
            readonly
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

```

# Vuetify component v-text-field - prop clearable

Example code

```vue
<template>
  <v-responsive
    class="mx-auto"
    max-width="344"
  >
    <v-text-field
      v-model="model"
      hide-details="auto"
      label="Last name"
      clearable
    ></v-text-field>
  </v-responsive>
</template>

<script setup>
  import { ref } from 'vue'

  const model = ref('Leider')
</script>

<script>
  export default {
    data: () => ({
      model: 'Leider',
    }),
  }
</script>

```

# Vuetify component v-text-field - prop counter

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="title"
            :rules="rules"
            counter="25"
            hint="This field uses counter prop"
            label="Regular"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="description"
            :rules="rules"
            hint="This field uses maxlength attribute"
            label="Limit exceeded"
            maxlength="25"
            counter
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="title"
            :counter-value="v => v.trim().split(' ').length"
            :rules="wordsRules"
            counter="5"
            hint="This field counts words instead of characters"
            label="Custom counter from prop"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="title"
            :rules="wordsRules"
            counter="5"
            hint="This field counts words instead of characters"
            label="Custom counter from slot"
          >
            <template v-slot:counter="{ props }">
              <v-counter v-bind="props" :value="title.trim().split(' ').length"></v-counter>
            </template>
          </v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
  import { ref } from 'vue'

  const rules = [v => v.length <= 25 || 'Max 25 characters']
  const wordsRules = [v => v.trim().split(' ').length <= 5 || 'Max 5 words']

  const title = ref('Preliminary report')
  const description = ref('California is a state in the western United States')
</script>

<script>
  export default {
    data () {
      return {
        title: 'Preliminary report',
        description: 'California is a state in the western United States',
        rules: [v => v.length <= 25 || 'Max 25 characters'],
        wordsRules: [v => v.trim().split(' ').length <= 5 || 'Max 5 words'],
      }
    },
  }
</script>

```

# Vuetify component v-text-field - prop rules

Example code

```vue
<template>
  <v-responsive
    class="mx-auto"
    max-width="344"
  >
    <v-text-field
      :rules="[rules.required]"
      label="Last name"
      clearable
    ></v-text-field>
  </v-responsive>
</template>

<script setup>
  const rules = {
    required: value => !!value || 'Field is required',
  }
</script>

<script>
  export default {
    data: () => ({
      rules: {
        required: value => !!value || 'Field is required',
      },
    }),
  }
</script>

```

# Vuetify component v-text-field - prop filled

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="first"
            label="First Name"
            variant="filled"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="last"
            label="Last Name"
            variant="filled"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
  import { ref } from 'vue'

  const first = ref('John')
  const last = ref('Doe')
</script>

<script>
  export default {
    data: () => ({
      first: 'John',
      last: 'Doe',
    }),
  }
</script>

```

# Vuetify component v-text-field - misc login form

Example code

```vue
<template>
  <div>
    <v-img
      class="mx-auto my-6"
      max-width="228"
      src="https://cdn.vuetifyjs.com/docs/images/logos/vuetify-logo-v3-slim-text-light.svg"
    ></v-img>

    <v-card
      class="mx-auto pa-12 pb-8"
      elevation="8"
      max-width="448"
      rounded="lg"
    >
      <div class="text-subtitle-1 text-medium-emphasis">Account</div>

      <v-text-field
        density="compact"
        placeholder="Email address"
        prepend-inner-icon="mdi-email-outline"
        variant="outlined"
      ></v-text-field>

      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
        Password

        <a
          class="text-caption text-decoration-none text-blue"
          href="#"
          rel="noopener noreferrer"
          target="_blank"
        >
          Forgot login password?</a>
      </div>

      <v-text-field
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="Enter your password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
      ></v-text-field>

      <v-card
        class="mb-12"
        color="surface-variant"
        variant="tonal"
      >
        <v-card-text class="text-medium-emphasis text-caption">
          Warning: After 3 consecutive failed login attempts, you account will be temporarily locked for three hours. If you must login now, you can also click "Forgot login password?" below to reset the login password.
        </v-card-text>
      </v-card>

      <v-btn
        class="mb-8"
        color="blue"
        size="large"
        variant="tonal"
        block
      >
        Log In
      </v-btn>

      <v-card-text class="text-center">
        <a
          class="text-blue text-decoration-none"
          href="#"
          rel="noopener noreferrer"
          target="_blank"
        >
          Sign up now <v-icon icon="mdi-chevron-right"></v-icon>
        </a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const visible = ref(false)
</script>

<script>
  export default {
    data: () => ({
      visible: false,
    }),
  }
</script>

```

# Vuetify component v-text-field - prop label

Example code

```vue
<template>
  <v-responsive
    class="mx-auto"
    max-width="344"
  >
    <v-text-field
      hide-details="auto"
      label="First name"
    ></v-text-field>
  </v-responsive>
</template>

```

# Vuetify component v-text-field - prop outlined

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="first"
            label="First Name"
            variant="outlined"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="last"
            label="Last Name"
            variant="outlined"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
  import { ref } from 'vue'

  const first = ref('John')
  const last = ref('Doe')
</script>

<script>
  export default {
    data: () => ({
      first: 'John',
      last: 'Doe',
    }),
  }
</script>

```

# Vuetify component v-text-field - slot progress

Example code

```vue
<template>
  <v-container fluid>
    <v-checkbox-btn
      v-model="custom"
      label="Loading"
    ></v-checkbox-btn>

    <v-text-field
      v-model="value"
      label="Type characters to change the loader color"
      placeholder="Start typing..."
      loading
    >
      <template v-slot:loader>
        <v-progress-linear
          :active="custom"
          :color="color"
          :model-value="progress"
          height="7"
          indeterminate
        ></v-progress-linear>
      </template>
    </v-text-field>
  </v-container>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const value = ref('')
  const custom = ref(false)
  const progress = computed(() => {
    return Math.min(100, value.value.length * 10)
  })
  const color = computed(() => {
    return ['error', 'warning', 'success'][Math.floor(progress.value / 40)]
  })
</script>

<script>
  export default {
    data: () => ({
      value: '',
      custom: false,
    }),

    computed: {
      progress () {
        return Math.min(100, this.value.length * 10)
      },
      color () {
        return ['error', 'warning', 'success'][Math.floor(this.progress / 40)]
      },
    },
  }
</script>

```

# Vuetify component v-text-field - misc password

Example code

```vue
<template>
  <v-form>
    <v-container fluid>
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            v-model="password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show1 ? 'text' : 'password'"
            hint="At least 8 characters"
            label="Normal with hint text"
            name="input-10-1"
            counter
            @click:append="show1 = !show1"
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show2 ? 'text' : 'password'"
            class="input-group--focused"
            hint="At least 8 characters"
            label="Visible"
            name="input-10-2"
            @click:append="show2 = !show2"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
  import { ref } from 'vue'

  const rules = {
    required: value => !!value || 'Required.',
    min: v => v.length >= 8 || 'Min 8 characters',
    emailMatch: () => (`The email and password you entered don't match`),
  }

  const show1 = ref(false)
  const show2 = ref(true)
  const password = ref('Password')
</script>

<script>
  export default {
    data () {
      return {
        show1: false,
        show2: true,
        password: 'Password',
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
          emailMatch: () => (`The email and password you entered don't match`),
        },
      }
    },
  }
</script>

```

# Vuetify component v-text-field - slot icons

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field
            v-model="message"
            label="Message"
            type="text"
            variant="outlined"
            clearable
          >
            <template v-slot:prepend>
              <v-tooltip location="bottom">
                <template v-slot:activator="{ props }">
                  <v-icon v-bind="props" icon="mdi-help-circle-outline"></v-icon>
                </template>

                I'm a tooltip
              </v-tooltip>
            </template>

            <template v-slot:append-inner>
              <v-fade-transition leave-absolute>
                <v-progress-circular
                  v-if="loading"
                  color="info"
                  size="24"
                  indeterminate
                ></v-progress-circular>

                <img
                  v-else
                  alt=""
                  height="24"
                  src="https://cdn.vuetifyjs.com/images/logos/v-alt.svg"
                  width="24"
                >
              </v-fade-transition>
            </template>

            <template v-slot:append>
              <v-menu>
                <template v-slot:activator="{ props }">
                  <v-btn v-bind="props" class="mt-n2">
                    <v-icon icon="mdi-menu" start></v-icon>

                    Menu
                  </v-btn>
                </template>

                <v-card>
                  <v-card-text class="pa-6">
                    <v-btn
                      color="primary"
                      size="large"
                      variant="text"
                      @click="clickMe"
                    >
                      <v-icon icon="mdi-target" start></v-icon>

                      Click me
                    </v-btn>
                  </v-card-text>
                </v-card>
              </v-menu>
            </template>
          </v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
  import { ref } from 'vue'

  const message = ref('Hey!')
  const loading = ref(false)

  function clickMe () {
    loading.value = true
    message.value = 'Wait for it...'
    setTimeout(() => {
      loading.value = false
      message.value = `You've clicked me!`
    }, 2000)
  }
</script>

<script>
  export default {
    data: () => ({
      message: 'Hey!',
      loading: false,
    }),

    methods: {
      clickMe () {
        this.loading = true
        this.message = 'Wait for it...'
        setTimeout(() => {
          this.loading = false
          this.message = `You've clicked me!`
        }, 2000)
      },
    },
  }
</script>

```

# Vuetify component v-text-field - prop single line

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Regular"
            single-line
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Solo"
            variant="solo"
            single-line
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Filled"
            variant="filled"
            single-line
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Outlined"
            variant="outlined"
            single-line
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

```

# Vuetify component v-text-field - misc full width with counter

Example code

```vue
<template>
  <v-form>
    <v-autocomplete
      v-model="selected"
      :items="items"
      label="To"
      chips
      hide-details
      hide-no-data
      hide-selected
      multiple
      single-line
    ></v-autocomplete>

    <v-divider></v-divider>

    <v-text-field
      v-model="subject"
      label="Subject"
      hide-details
      single-line
    ></v-text-field>

    <v-divider></v-divider>

    <v-textarea
      v-model="title"
      label="Message"
      maxlength="120"
      counter
      single-line
    ></v-textarea>
  </v-form>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ['Trevor Handsen', 'Alex Nelson']

  const selected = ref(['Trevor Handsen'])
  const subject = ref('Plans for the weekend')
  const title = ref('Hi,\nI just wanted to check in and see if you had any plans the upcoming weekend. We are thinking of heading up to Napa')
</script>

<script>
  export default {
    data: () => ({
      items: ['Trevor Handsen', 'Alex Nelson'],
      selected: ['Trevor Handsen'],
      subject: 'Plans for the weekend',
      title: 'Hi,\nI just wanted to check in and see if you had any plans the upcoming weekend. We are thinking of heading up to Napa',
    }),
  }
</script>

```

# Vuetify component v-text-field - misc custom validation

Example code

```vue
<template>
  <v-row justify="center">
    <v-col
      cols="12"
      lg="6"
      md="8"
      sm="10"
    >
      <v-card ref="form">
        <v-card-text>
          <v-text-field
            ref="name"
            v-model="name"
            :error-messages="errorMessages"
            :rules="[() => !!name || 'This field is required']"
            label="Full Name"
            placeholder="John Doe"
            required
          ></v-text-field>
          <v-text-field
            ref="address"
            v-model="address"
            :rules="[
              () => !!address || 'This field is required',
              () => !!address && address.length <= 25 || 'Address must be less than 25 characters',
              addressCheck
            ]"
            counter="25"
            label="Address Line"
            placeholder="Snowy Rock Pl"
            required
          ></v-text-field>
          <v-text-field
            ref="city"
            v-model="city"
            :rules="[() => !!city || 'This field is required', addressCheck]"
            label="City"
            placeholder="El Paso"
            required
          ></v-text-field>
          <v-text-field
            ref="state"
            v-model="state"
            :rules="[() => !!state || 'This field is required']"
            label="State/Province/Region"
            placeholder="TX"
            required
          ></v-text-field>
          <v-text-field
            ref="zip"
            v-model="zip"
            :rules="[() => !!zip || 'This field is required']"
            label="ZIP / Postal Code"
            placeholder="79938"
            required
          ></v-text-field>
          <v-autocomplete
            ref="country"
            v-model="country"
            :items="countries"
            :rules="[() => !!country || 'This field is required']"
            label="Country"
            placeholder="Select..."
            required
          ></v-autocomplete>
        </v-card-text>
        <v-divider class="mt-12"></v-divider>
        <v-card-actions>
          <v-btn variant="text">
            Cancel
          </v-btn>
          <v-spacer></v-spacer>
          <v-slide-x-reverse-transition>
            <v-tooltip
              v-if="formHasErrors"
              location="left"
            >
              <template v-slot:activator="{ props }">
                <v-btn
                  icon
                  v-bind="props"
                  @click="resetForm"
                >
                  <v-icon>mdi-refresh</v-icon>
                </v-btn>
              </template>
              <span>Refresh form</span>
            </v-tooltip>
          </v-slide-x-reverse-transition>
          <v-btn
            color="primary"
            variant="text"
            @click="submit"
          >
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data: () => ({
      countries: ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua &amp; Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia &amp; Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Cape Verde', 'Cayman Islands', 'Chad', 'Chile', 'China', 'Colombia', 'Congo', 'Cook Islands', 'Costa Rica', 'Cote D Ivoire', 'Croatia', 'Cruise Ship', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'French West Indies', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyz Republic', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Pierre &amp; Miquelon', 'Samoa', 'San Marino', 'Satellite', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'St Kitts &amp; Nevis', 'St Lucia', 'St Vincent', 'St. Lucia', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', `Timor L'Este`, 'Togo', 'Tonga', 'Trinidad &amp; Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks &amp; Caicos', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Virgin Islands (US)', 'Yemen', 'Zambia', 'Zimbabwe'],
      errorMessages: '',
      name: null,
      address: null,
      city: null,
      state: null,
      zip: null,
      country: null,
      formHasErrors: false,
    }),

    computed: {
      form () {
        return {
          name: this.name,
          address: this.address,
          city: this.city,
          state: this.state,
          zip: this.zip,
          country: this.country,
        }
      },
    },

    watch: {
      name () {
        this.errorMessages = ''
      },
    },

    methods: {
      addressCheck () {
        this.errorMessages = this.address && !this.name
          ? `Hey! I'm required`
          : ''

        return true
      },
      resetForm () {
        this.errorMessages = []
        this.formHasErrors = false

        Object.keys(this.form).forEach(f => {
          this.$refs[f].reset()
        })
      },
      submit () {
        this.formHasErrors = false

        Object.keys(this.form).forEach(f => {
          if (!this.form[f]) this.formHasErrors = true

          this.$refs[f].validate(true)
        })
      },
    },
  }
</script>

```

# Vuetify component v-text-field - prop custom colors

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="344"
    title="User Registration"
  >
    <v-container>
      <v-text-field
        v-model="first"
        color="primary"
        label="First name"
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model="last"
        color="primary"
        label="Last name"
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model="email"
        color="primary"
        label="Email"
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model="password"
        color="primary"
        label="Password"
        placeholder="Enter your password"
        variant="underlined"
      ></v-text-field>

      <v-checkbox
        v-model="terms"
        color="secondary"
        label="I agree to site terms and conditions"
      ></v-checkbox>
    </v-container>

    <v-divider></v-divider>

    <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn color="success">
        Complete Registration

        <v-icon icon="mdi-chevron-right" end></v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const first = ref(null)
  const last = ref(null)
  const email = ref(null)
  const password = ref(null)
  const terms = ref(false)
</script>

<script>
  export default {
    data: () => ({
      first: null,
      last: null,
      email: null,
      password: null,
      terms: false,
    }),
  }
</script>

```

# Vuetify component v-text-field - misc guide

Example code

```vue
<template>
  <v-sheet class="bg-deep-purple pa-12" rounded>
    <v-card class="mx-auto px-6 py-8" max-width="344">
      <v-form
        v-model="form"
        @submit.prevent="onSubmit"
      >
        <v-text-field
          v-model="email"
          :readonly="loading"
          :rules="[required]"
          class="mb-2"
          label="Email"
          clearable
        ></v-text-field>

        <v-text-field
          v-model="password"
          :readonly="loading"
          :rules="[required]"
          label="Password"
          placeholder="Enter your password"
          clearable
        ></v-text-field>

        <br>

        <v-btn
          :disabled="!form"
          :loading="loading"
          color="success"
          size="large"
          type="submit"
          variant="elevated"
          block
        >
          Sign In
        </v-btn>
      </v-form>
    </v-card>
  </v-sheet>
</template>

<script setup>
  import { ref } from 'vue'

  const form = ref(false)
  const email = ref(null)
  const password = ref(null)
  const loading = ref(false)

  function onSubmit () {
    if (!form.value) return
    loading.value = true
    setTimeout(() => (loading.value = false), 2000)
  }
  function required (v) {
    return !!v || 'Field is required'
  }
</script>

<script>
  export default {
    data: () => ({
      form: false,
      email: null,
      password: null,
      loading: false,
    }),

    methods: {
      onSubmit () {
        if (!this.form) return

        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
      required (v) {
        return !!v || 'Field is required'
      },
    },
  }
</script>

```

# Vuetify component v-text-field - prop prefixes and suffixes

Example code

```vue
<template>
  <v-container fluid>
    <v-row>
      <v-col cols="4">
        <v-list-subheader>Prefix for dollar currency</v-list-subheader>
      </v-col>

      <v-col cols="8">
        <v-text-field
          label="Amount"
          model-value="10.00"
          prefix="$"
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="4">
        <v-list-subheader>Suffix for weight</v-list-subheader>
      </v-col>

      <v-col cols="8">
        <v-text-field
          label="Weight"
          model-value="28.00"
          suffix="lbs"
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="4">
        <v-list-subheader>Suffix for email domain</v-list-subheader>
      </v-col>

      <v-col cols="8">
        <v-text-field
          label="Email address"
          model-value="example"
          suffix="@gmail.com"
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="4">
        <v-list-subheader>Suffix for time zone</v-list-subheader>
      </v-col>

      <v-col cols="8">
        <v-text-field
          label="Label Text"
          model-value="12:30:00"
          suffix="PST"
          type="time"
        ></v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-text-field - prop hide details

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

# Vuetify component v-text-field - slot label

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-text-field>
        <template v-slot:label>
          <span>
            What about an <strong>icon</strong> here? <v-icon icon="mdi-file-find"></v-icon>
          </span>
        </template>
      </v-text-field>
    </v-container>
  </v-form>
</template>

```

# Vuetify component v-text-field - event icons

Example code

```vue
<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field
            v-model="message"
            :append-icon="message ? 'mdi-send' : 'mdi-microphone'"
            :append-inner-icon="marker ? 'mdi-map-marker' : 'mdi-map-marker-off'"
            :prepend-icon="icon"
            clear-icon="mdi-close-circle"
            label="Message"
            type="text"
            variant="filled"
            clearable
            @click:append="sendMessage"
            @click:append-inner="toggleMarker"
            @click:clear="clearMessage"
            @click:prepend="changeIcon"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const icons = [
    'mdi-emoticon',
    'mdi-emoticon-cool',
    'mdi-emoticon-dead',
    'mdi-emoticon-excited',
    'mdi-emoticon-happy',
    'mdi-emoticon-neutral',
    'mdi-emoticon-sad',
    'mdi-emoticon-tongue',
  ]

  const message = ref('Hey!')
  const marker = ref(true)
  const iconIndex = ref(0)

  const icon = computed(() => {
    return icons[iconIndex.value]
  })
  function toggleMarker () {
    marker.value = !marker.value
  }

  function sendMessage () {
    resetIcon()
    clearMessage()
  }
  function clearMessage () {
    message.value = ''
  }
  function resetIcon () {
    iconIndex.value = 0
  }
  function changeIcon () {
    iconIndex.value === icons.length - 1
      ? iconIndex.value = 0
      : iconIndex.value++
  }
</script>

<script>
  export default {
    data: () => ({
      message: 'Hey!',
      marker: true,
      iconIndex: 0,
      icons: [
        'mdi-emoticon',
        'mdi-emoticon-cool',
        'mdi-emoticon-dead',
        'mdi-emoticon-excited',
        'mdi-emoticon-happy',
        'mdi-emoticon-neutral',
        'mdi-emoticon-sad',
        'mdi-emoticon-tongue',
      ],
    }),

    computed: {
      icon () {
        return this.icons[this.iconIndex]
      },
    },

    methods: {
      toggleMarker () {
        this.marker = !this.marker
      },
      sendMessage () {
        this.resetIcon()
        this.clearMessage()
      },
      clearMessage () {
        this.message = ''
      },
      resetIcon () {
        this.iconIndex = 0
      },
      changeIcon () {
        this.iconIndex === this.icons.length - 1
          ? this.iconIndex = 0
          : this.iconIndex++
      },
    },
  }
</script>

```
