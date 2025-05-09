# Vuetify component v-window - usage

Example code

```vue
<template>
  <v-window
    v-model="window"
    show-arrows
  >
    <v-window-item
      v-for="n in length"
      :key="n"
    >
      <v-card class="d-flex justify-center align-center" height="200px">
        <span class="text-h2">Card {{ n }}</span>
      </v-card>
    </v-window-item>
  </v-window>
</template>

<script>
  export default {
    data: () => ({
      length: 3,
      window: 0,
    }),
  }
</script>

```

# Vuetify component v-window - misc account creation

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-card-title class="text-h6 font-weight-regular justify-space-between">
      <span>{{ currentTitle }}</span>
      <v-avatar
        color="primary"
        size="24"
        v-text="step"
      ></v-avatar>
    </v-card-title>

    <v-window v-model="step">
      <v-window-item :value="1">
        <v-card-text>
          <v-text-field
            label="Email"
            placeholder="john@google.com"
          ></v-text-field>
          <span class="text-caption text-grey-darken-1">
            This is the email you will use to login to your Vuetify account
          </span>
        </v-card-text>
      </v-window-item>

      <v-window-item :value="2">
        <v-card-text>
          <v-text-field
            label="Password"
            type="password"
          ></v-text-field>
          <v-text-field
            label="Confirm Password"
            type="password"
          ></v-text-field>
          <span class="text-caption text-grey-darken-1">
            Please enter a password for your account
          </span>
        </v-card-text>
      </v-window-item>

      <v-window-item :value="3">
        <div class="pa-4 text-center">
          <v-img
            class="mb-4"
            height="128"
            src="https://cdn.vuetifyjs.com/images/logos/v.svg"
          ></v-img>
          <h3 class="text-h6 font-weight-light mb-2">
            Welcome to Vuetify
          </h3>
          <span class="text-caption text-grey">Thanks for signing up!</span>
        </div>
      </v-window-item>
    </v-window>

    <v-divider></v-divider>

    <v-card-actions>
      <v-btn
        v-if="step > 1"
        variant="text"
        @click="step--"
      >
        Back
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        v-if="step < 3"
        color="primary"
        variant="flat"
        @click="step++"
      >
        Next
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const step = ref(1)

  const currentTitle = computed(() => {
    switch (step.value) {
      case 1: return 'Sign-up'
      case 2: return 'Create a password'
      default: return 'Account created'
    }
  })
</script>

<script>
  export default {
    data: () => ({
      step: 1,
    }),

    computed: {
      currentTitle () {
        switch (this.step) {
          case 1: return 'Sign-up'
          case 2: return 'Create a password'
          default: return 'Account created'
        }
      },
    },
  }
</script>

```

# Vuetify component v-window - prop reverse

Example code

```vue
<template>
  <v-window
    v-model="onboarding"
    reverse
    show-arrows
  >
    <v-window-item
      v-for="n in length"
      :key="`card-${n}`"
    >
      <v-card
        class="d-flex align-center justify-center ma-2"
        elevation="2"
        height="200"
      >
        <h1
          class="text-h2"
        >
          Slide {{ n }}
        </h1>
      </v-card>
    </v-window-item>
  </v-window>
</template>

<script setup>
  import { ref } from 'vue'

  const length = ref(3)
  const onboarding = ref(0)
</script>

<script>
  export default {
    data: () => ({
      length: 3,
      onboarding: 0,
    }),
  }
</script>

```

# Vuetify component v-window - prop direction

Example code

```vue
<template>
  <v-window
    v-model="onboarding"
    direction="vertical"
    show-arrows
  >
    <v-window-item
      v-for="n in length"
      :key="`card-${n}`"
    >
      <v-card
        class="d-flex align-center justify-center ma-2"
        elevation="2"
        height="200"
      >
        <h1
          class="text-h2"
        >
          Slide {{ n }}
        </h1>
      </v-card>
    </v-window-item>
  </v-window>
</template>

<script setup>
  import { ref } from 'vue'

  const length = ref(3)
  const onboarding = ref(0)
</script>

<script>
  export default {
    data: () => ({
      length: 3,
      onboarding: 0,
    }),
  }
</script>

```

# Vuetify component v-window - slots next prev

Example code

```vue
<template>
  <v-window show-arrows>
    <template v-slot:prev="{ props }">
      <v-btn
        color="success"
        @click="props.onClick"
      >
        Previous slide
      </v-btn>
    </template>
    <template v-slot:next="{ props }">
      <v-btn
        color="info"
        @click="props.onClick"
      >
        Next slide
      </v-btn>
    </template>
    <v-window-item
      v-for="n in 3"
      :key="`card-${n}`"
    >
      <v-card
        class="d-flex align-center justify-center ma-2"
        elevation="2"
        height="200"
      >
        <h1
          class="text-h2"
        >
          Slide {{ n }}
        </h1>
      </v-card>
    </v-window-item>
  </v-window>
</template>

```

# Vuetify component v-window - misc onboarding

Example code

```vue
<template>
  <v-card
    rounded="0"
    theme="dark"
    flat
  >
    <v-window v-model="onboarding">
      <v-window-item
        v-for="n in length"
        :key="`card-${n}`"
        :value="n"
      >
        <v-card
          class="d-flex justify-center align-center"
          height="200"
        >
          <span class="text-h2">
            Card {{ n }}
          </span>
        </v-card>
      </v-window-item>
    </v-window>

    <v-card-actions class="justify-space-between">
      <v-btn
        icon="mdi-chevron-left"
        variant="plain"
        @click="prev"
      ></v-btn>
      <v-item-group
        v-model="onboarding"
        class="text-center"
        mandatory
      >
        <v-item
          v-for="n in length"
          :key="`btn-${n}`"
          v-slot="{ isSelected, toggle }"
          :value="n"
        >
          <v-btn
            :variant="isSelected ? 'outlined' : 'text'"
            icon="mdi-record"
            @click="toggle"
          ></v-btn>
        </v-item>
      </v-item-group>
      <v-btn
        icon="mdi-chevron-right"
        variant="plain"
        @click="next"
      ></v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const length = ref(3)
  const onboarding = ref(1)

  function next () {
    onboarding.value = onboarding.value + 1 > length.value ? 1 : onboarding.value + 1
  }
  function prev () {
    onboarding.value = onboarding.value - 1 <= 0 ? length.value : onboarding.value - 1
  }
</script>

<script>
  export default {
    data: () => ({
      length: 3,
      onboarding: 1,
    }),

    methods: {
      next () {
        this.onboarding = this.onboarding + 1 > this.length
          ? 1
          : this.onboarding + 1
      },
      prev () {
        this.onboarding = this.onboarding - 1 <= 0
          ? this.length
          : this.onboarding - 1
      },
    },
  }
</script>

```

# Vuetify component v-window - prop show arrows

Example code

```vue
<template>
  <v-window
    v-model="onboarding"
    show-arrows="hover"
  >
    <v-window-item
      v-for="n in length"
      :key="`card-${n}`"
    >
      <v-card
        class="d-flex align-center justify-center ma-2"
        elevation="2"
        height="200"
      >
        <h1
          class="text-h2"
        >
          Slide {{ n }}
        </h1>
      </v-card>
    </v-window-item>
  </v-window>
</template>

<script setup>
  import { ref } from 'vue'

  const length = ref(3)
  const onboarding = ref(0)
</script>

<script>
  export default {
    data: () => ({
      length: 3,
      onboarding: 0,
    }),
  }
</script>

```
