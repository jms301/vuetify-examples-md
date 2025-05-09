# Vuetify component v-otp-input - usage

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
      <v-otp-input v-bind="props"></v-otp-input>
    </div>

    <template v-slot:configuration>
      <v-text-field v-model="placeholder" label="Placeholder" maxlength="1" clearable></v-text-field>
      <v-checkbox v-model="focus" label="Focus all"></v-checkbox>
      <v-checkbox v-model="disabled" label="Disabled"></v-checkbox>
      <v-checkbox v-model="loading" label="Loading"></v-checkbox>
      <v-slider v-model="length" label="Length" max="8" min="4" step="1"></v-slider>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-stepper'
  const model = ref('default')
  const options = ['solo', 'solo-filled', 'underlined']
  const focus = ref(false)
  const length = ref(6)
  const placeholder = ref('')
  const disabled = ref(false)
  const loading = ref(false)

  const props = computed(() => {
    return {
      disabled: disabled.value || undefined,
      'focus-all': focus.value || undefined,
      length: length.value === 6 ? undefined : length.value,
      loading: loading.value || undefined,
      placeholder: placeholder.value || undefined,
      variant: model.value !== 'default' ? model.value : undefined,
    }
  })

  const slots = computed(() => {
    return ``
  })

  const code = computed(() => {
    return `<v-otp-input${propsToString(props.value)}>${slots.value}</v-otp-input>`
  })
</script>

```

# Vuetify component v-otp-input - prop loader

Example code

```vue
<template>
  <div class="text-center">
    <v-otp-input
      v-model="otp"
      :loading="loading"
      length="5"
      variant="underlined"
    ></v-otp-input>

    <v-btn
      :disabled="otp.length < 5 || loading"
      class="my-5"
      color="surface-variant"
      text="Submit"
      variant="tonal"
      @click="onClick"
    ></v-btn>
  </div>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const loading = shallowRef(false)
  const otp = shallowRef('31')

  function onClick () {
    loading.value = true

    setTimeout(() => {
      loading.value = false
    }, 2000)
  }
</script>

<script>
  export default {
    data: () => ({
      loading: false,
      otp: '',
    }),

    methods: {
      onClick () {
        this.loading = true

        setTimeout(() => {
          this.loading = false
        }, 2000)
      },
    },
  }
</script>

```

# Vuetify component v-otp-input - prop variant

Example code

```vue
<template>
  <v-otp-input
    model-value="8011"
    variant="filled"
  ></v-otp-input>
</template>

```

# Vuetify component v-otp-input - prop length

Example code

```vue
<template>
  <v-otp-input
    length="7"
    model-value="3214214"
  ></v-otp-input>
</template>

```

# Vuetify component v-otp-input - misc card

Example code

```vue
<template>
  <v-card
    class="py-8 px-6 text-center mx-auto ma-4"
    elevation="12"
    max-width="400"
    width="100%"
  >
    <h3 class="text-h6 mb-4">Verify Your Account</h3>

    <div class="text-body-2">
      We sent a verification code to john..@gmail.com <br>

      Please check your email and paste the code below.
    </div>

    <v-sheet color="surface">
      <v-otp-input
        v-model="otp"
        type="password"
        variant="solo"
      ></v-otp-input>
    </v-sheet>

    <v-btn
      class="my-4"
      color="purple"
      height="40"
      text="Verify"
      variant="flat"
      width="70%"
    ></v-btn>

    <div class="text-caption">
      Didn't receive the code? <a href="#" @click.prevent="otp = ''">Resend</a>
    </div>
  </v-card>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const otp = shallowRef('')
</script>

<script>
  export default {
    data: () => ({
      otp: '',
    }),
  }
</script>

```

# Vuetify component v-otp-input - prop error

Example code

```vue
<template>
  <v-otp-input
    model-value="221"
    error
  ></v-otp-input>
</template>

```

# Vuetify component v-otp-input - misc mobile

Example code

```vue
<template>
  <v-sheet
    class="pt-8 pb-12 px-6 ma-4 mx-auto"
    max-width="350"
    width="100%"
    border
  >
    <h3 class="text-h6 mb-1">Mobile phone verification</h3>

    <div class="text-body-2 font-weight-light">
      Enter the code we just sent to your mobile phone <span class="font-weight-black text-primary">+1 408 555 1212</span>
    </div>

    <v-otp-input
      v-model="otp"
      class="mt-3 ms-n2"
      length="4"
      placeholder="0"
      variant="underlined"
    ></v-otp-input>

    <v-divider class="mt-3 mb-6"></v-divider>

    <div class="mb-3 text-body-2">
      Need another <strong>code</strong>?
    </div>

    <v-btn
      color="primary"
      size="small"
      text="Re-send Email"
      variant="tonal"
      @click="otp = ''"
    ></v-btn>
  </v-sheet>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const otp = shallowRef('')
</script>

<script>
  export default {
    data: () => ({
      otp: '',
    }),
  }
</script>

```

# Vuetify component v-otp-input - prop focus all

Example code

```vue
<template>
  <v-otp-input
    model-value="425"
    focus-all
    focused
  ></v-otp-input>
</template>

```

# Vuetify component v-otp-input - misc verify

Example code

```vue
<template>
  <v-card
    class="py-12 px-8 text-center mx-auto ma-4"
    max-width="420"
    width="100%"
  >
    <h3 class="text-h6 mb-2">
      Please enter the one time password to verify your account
    </h3>

    <div>A code has been sent to *****2489</div>

    <v-otp-input
      v-model="otp"
      :disabled="validating"
      color="primary"
      variant="plain"
    ></v-otp-input>

    <v-btn
      :loading="validating"
      class="mt-6 text-none bg-surface-variant"
      height="40"
      text="Validate"
      variant="plain"
      width="135"
      border
      rounded
      @click="onClick"
    ></v-btn>
  </v-card>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const otp = shallowRef('2401')
  const validating = shallowRef(false)

  function onClick () {
    validating.value = true

    setTimeout(() => {
      validating.value = false
    }, 2000)
  }
</script>

<script>
  export default {
    data: () => ({
      otp: '',
      validating: false,
    }),

    methods: {
      onClick () {
        this.validating = true

        setTimeout(() => {
          this.validating = false
        }, 2000)
      },
    },
  }
</script>

```

# Vuetify component v-otp-input - misc divider

Example code

```vue
<template>
  <v-sheet
    class="py-8 px-6 mx-auto ma-4 text-center"
    elevation="4"
    max-width="500"
    rounded="lg"
    width="100%"
  >
    <h3 class="text-h5">Verification Code</h3>

    <div class="text-subtitle-2 font-weight-light mb-3">Please enter the verification code sent to your mobile</div>

    <v-otp-input
      v-model="otp"
      class="mb-8"
      divider="•"
      length="4"
      variant="outlined"
    ></v-otp-input>

    <div class="text-caption">
      <v-btn
        color="primary"
        size="x-small"
        text="Send New Code"
        variant="text"
        @click="otp = ''"
      ></v-btn>
    </div>
  </v-sheet>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const otp = shallowRef('')
</script>

<script>
  export default {
    data: () => ({
      otp: '',
    }),
  }
</script>

```
