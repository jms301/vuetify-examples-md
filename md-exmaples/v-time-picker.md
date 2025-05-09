# Vuetify component v-time-picker - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <v-row justify="center">
      <v-time-picker v-bind="props"></v-time-picker>
    </v-row>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-time-picker'
  const model = ref('default')
  const options = []

  const props = computed(() => {
    return {
      //
    }
  })

  const slots = computed(() => {
    return ''
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-time-picker - prop hide header

Example code

```vue
<template>
  <v-container>
    <v-row justify="center">
      <v-time-picker hide-header></v-time-picker>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-time-picker - prop use seconds

Example code

```vue
<template>
  <v-container>
    <v-row justify="center">
      <v-time-picker use-seconds></v-time-picker>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-time-picker - misc dialog and menu

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-col
        cols="11"
        sm="5"
      >
        <v-text-field
          v-model="time"
          :active="menu2"
          :focus="menu2"
          label="Picker in menu"
          prepend-icon="mdi-clock-time-four-outline"
          readonly
        >
          <v-menu
            v-model="menu2"
            :close-on-content-click="false"
            activator="parent"
            transition="scale-transition"
          >
            <v-time-picker
              v-if="menu2"
              v-model="time"
              full-width
            ></v-time-picker>
          </v-menu>
        </v-text-field>
      </v-col>

      <v-col
        cols="11"
        sm="5"
      >
        <v-text-field
          v-model="time"
          :active="modal2"
          :focused="modal2"
          label="Picker in dialog"
          prepend-icon="mdi-clock-time-four-outline"
          readonly
        >
          <v-dialog
            v-model="modal2"
            activator="parent"
            width="auto"
          >
            <v-time-picker
              v-if="modal2"
              v-model="time"
            ></v-time-picker>
          </v-dialog>
        </v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const time = ref(null)
  const menu2 = ref(false)
  const modal2 = ref(false)
</script>

<script>
  export default {
    data () {
      return {
        time: null,
        menu2: false,
        modal2: false,
      }
    },
  }
</script>

```

# Vuetify component v-time-picker - prop elevation

Example code

```vue
<template>
  <v-container>
    <v-row justify="center">
      <v-time-picker
        elevation="15"
      ></v-time-picker>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-time-picker - prop allowed times

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-time-picker
        v-model="time"
        :allowed-hours="allowedHours"
        :allowed-minutes="allowedMinutes"
        format="24hr"
        max="22:15"
        min="9:30"
        scrollable
      ></v-time-picker>

      <v-time-picker
        v-model="timeStep"
        :allowed-minutes="allowedStep"
        format="24hr"
      ></v-time-picker>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const time = ref('11:15')
  const timeStep = ref('10:10')

  const allowedHours = v => v % 2
  const allowedMinutes = v => v >= 10 && v <= 50
  const allowedStep = m => m % 10 === 0
</script>

<script>
  export default {
    data () {
      return {
        time: '11:15',
        timeStep: '10:10',
      }
    },
    methods: {
      allowedHours: v => v % 2,
      allowedMinutes: v => v >= 10 && v <= 50,
      allowedStep: m => m % 10 === 0,
    },
  }
</script>

```

# Vuetify component v-time-picker - prop ampm in title

Example code

```vue
<template>
  <v-row

    align="center"
    justify="space-around"
  >
    <v-time-picker
      v-model="picker"
      ampm-in-title
    ></v-time-picker>
    <v-time-picker
      v-model="picker"
      :landscape="$vuetify.display.smAndUp"
      ampm-in-title
    ></v-time-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const picker = ref(null)
</script>

<script>
  export default {
    data () {
      return {
        picker: null,
      }
    },
  }
</script>

```

# Vuetify component v-time-picker - prop scrollable

Example code

```vue
<template>
  <v-row
    align="center"
    justify="space-around"
  >
    <v-time-picker
      v-model="picker"
      scrollable
    ></v-time-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const picker = ref(null)
</script>

<script>
  export default {
    data () {
      return {
        picker: null,
      }
    },
  }
</script>

```

# Vuetify component v-time-picker - prop readonly

Example code

```vue
<template>
  <v-container>
    <v-row justify="center">
      <v-time-picker readonly></v-time-picker>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-time-picker - prop range

Example code

```vue
<template>
  <div>
    <h1>Plan your event:</h1>
    <v-row
      align="center"
      justify="space-around"
    >
      <v-col style="width: 350px; flex: 0 1 auto;">
        <h2>Start:</h2>
        <v-time-picker
          v-model="start"
          :max="end"
        ></v-time-picker>
      </v-col>
      <v-col style="width: 350px; flex: 0 1 auto;">
        <h2>End:</h2>
        <v-time-picker
          v-model="end"
          :min="start"
        ></v-time-picker>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const start = ref(null)
  const end = ref(null)
</script>

<script>
  export default {
    data () {
      return {
        start: null,
        end: null,
      }
    },
  }
</script>

```

# Vuetify component v-time-picker - prop disabled

Example code

```vue
<template>
  <v-row
    align="center"
    justify="space-around"
  >
    <v-time-picker
      v-model="picker"
      disabled
    ></v-time-picker>
    <v-time-picker
      v-model="picker"
      :landscape="$vuetify.display.smAndUp"
      disabled
    ></v-time-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const picker = ref(null)
</script>

<script>
  export default {
    data () {
      return {
        picker: null,
      }
    },
  }
</script>

```

# Vuetify component v-time-picker - prop color

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-time-picker
        color="green-lighten-1"
      ></v-time-picker>

      <v-time-picker
        color="pink"
        header-color="primary"
      ></v-time-picker>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-time-picker - prop format

Example code

```vue
<template>
  <v-container>
    <v-row justify="center">
      <v-time-picker format="24hr"></v-time-picker>
    </v-row>
  </v-container>
</template>

```
