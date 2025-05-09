# Vuetify component v-date-picker-month - usage

Example code

```vue
<template>
  <v-row justify="center">
    <v-date-picker
      v-model="picker"
      type="month"
    ></v-date-picker>
  </v-row>
</template>

<script>
  export default {
    data () {
      return {
        picker: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      }
    },
  }
</script>

```

# Vuetify component v-date-picker-month - misc dialog and menu

Example code

```vue
<template>
  <v-row>
    <v-col
      cols="11"
      sm="5"
    >
      <v-menu
        ref="menu"
        v-model="menuActive"
        v-model:return-value="date"
        :close-on-content-click="false"
        max-width="290px"
        min-width="auto"
        transition="scale-transition"
      >
        <template v-slot:activator="{ props }">
          <v-text-field
            v-model="date"
            label="Picker in menu"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="props"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="date"
          type="month"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            variant="text"
            @click="menu = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="primary"
            variant="text"
            @click="menu.save(date)"
          >
            OK
          </v-btn>
        </v-date-picker>
      </v-menu>
    </v-col>
    <v-spacer></v-spacer>
    <v-col
      cols="11"
      sm="5"
    >
      <v-dialog
        ref="dialog"
        v-model="modal"
        v-model:return-value="date"
        width="290px"
        persistent
      >
        <template v-slot:activator="{ props }">
          <v-text-field
            v-model="date"
            label="Picker in dialog"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="props"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="date"
          type="month"
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            variant="text"
            @click="modal = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="primary"
            variant="text"
            @click="dialog.save(date)"
          >
            OK
          </v-btn>
        </v-date-picker>
      </v-dialog>
    </v-col>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const menu = ref()
  const dialog = ref()

  const date = ref(new Date().toISOString().substr(0, 7))
  const menuActive = ref(false)
  const modal = ref(false)
</script>

<script>
  export default {
    data: () => ({
      date: new Date().toISOString().substr(0, 7),
      menuActive: false,
      modal: false,
    }),
  }
</script>

```

# Vuetify component v-date-picker-month - prop width

Example code

```vue
<template>
  <v-row justify="space-around">
    <v-date-picker
      v-model="date"
      class="mt-4"
      type="month"
      width="290"
    ></v-date-picker>
    <v-date-picker
      v-model="date"
      class="mt-4"
      type="month"
      full-width
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const date = ref(new Date().toISOString().substr(0, 7))
</script>

<script>
  export default {
    data: () => ({
      date: new Date().toISOString().substr(0, 7),
    }),
  }
</script>

```

# Vuetify component v-date-picker-month - prop multiple

Example code

```vue
<template>
  <v-row justify="center">
    <v-date-picker
      v-model="months"
      type="month"
      multiple
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const months = ref(['2018-09', '2018-10'])
</script>

<script>
  export default {
    data: () => ({
      months: ['2018-09', '2018-10'],
    }),
  }
</script>

```

# Vuetify component v-date-picker-month - prop icons

Example code

```vue
<template>
  <v-row justify="center">
    <v-date-picker
      v-model="picker"
      next-icon="mdi-skip-next"
      prev-icon="mdi-skip-previous"
      type="month"
      year-icon="mdi-calendar-blank"
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const picker = ref(new Date().toISOString().substr(0, 7))
</script>

<script>
  export default {
    data () {
      return {
        picker: new Date().toISOString().substr(0, 7),
      }
    },
  }
</script>

```

# Vuetify component v-date-picker-month - prop readonly

Example code

```vue
<template>
  <v-row justify="center">
    <v-date-picker
      v-model="date"
      type="month"
      readonly
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const date = ref(new Date().toISOString().substr(0, 7))
</script>

<script>
  export default {
    data () {
      return {
        date: new Date().toISOString().substr(0, 7),
      }
    },
  }
</script>

```

# Vuetify component v-date-picker-month - prop allowed months

Example code

```vue
<template>
  <v-row justify="center">
    <v-date-picker
      v-model="date"
      :allowed-dates="allowedMonths"
      class="mt-4"
      max="2019-10"
      min="2017-06"
      type="month"
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const date = ref('2017-12')
</script>

<script>
  export default {
    data () {
      return {
        date: '2017-12',
      }
    },

    methods: {
      allowedMonths: val => parseInt(val.split('-')[1], 10) % 2 === 0,
    },
  }
</script>

```

# Vuetify component v-date-picker-month - misc orientation

Example code

```vue
<template>
  <v-row align="center">
    <v-checkbox
      v-model="landscape"
      label="Landscape"
    ></v-checkbox>
    <v-date-picker
      v-model="picker"
      :landscape="landscape"
      type="month"
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const picker = ref(new Date().toISOString().substr(0, 7))
  const landscape = ref(false)
</script>

<script>
  export default {
    data () {
      return {
        picker: new Date().toISOString().substr(0, 7),
        landscape: false,
      }
    },
  }
</script>

```

# Vuetify component v-date-picker-month - prop show current

Example code

```vue
<template>
  <v-row justify="space-around">
    <v-date-picker
      v-model="month1"
      :show-current="false"
      type="month"
    ></v-date-picker>
    <v-date-picker
      v-model="month2"
      show-current="2013-07"
      type="month"
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const month1 = ref(new Date().toISOString().substr(0, 7))
  const month2 = ref('2013-09')
</script>

<script>
  export default {
    data () {
      return {
        month1: new Date().toISOString().substr(0, 7),
        month2: '2013-09',
      }
    },
  }
</script>

```

# Vuetify component v-date-picker-month - misc internationalization

Example code

```vue
<template>
  <v-row justify="space-around">
    <v-date-picker
      v-model="picker"
      locale="th"
      type="month"
    ></v-date-picker>
    <v-date-picker
      v-model="picker"
      locale="sv-se"
      type="month"
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const picker = ref(new Date().toISOString().substr(0, 7))
</script>

<script>
  export default {
    data () {
      return {
        picker: new Date().toISOString().substr(0, 7),
      }
    },
  }
</script>

```

# Vuetify component v-date-picker-month - prop colors

Example code

```vue
<template>
  <v-row justify="space-around">
    <v-date-picker
      v-model="picker"
      color="green-lighten-1"
      type="month"
    ></v-date-picker>
    <v-date-picker
      v-model="picker2"
      color="green-lighten-1"
      header-color="primary"
      type="month"
    ></v-date-picker>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const picker = ref(new Date().toISOString().substr(0, 7))
  const picker2 = ref(new Date().toISOString().substr(0, 7))
</script>

<script>
  export default {
    data () {
      return {
        picker: new Date().toISOString().substr(0, 7),
        picker2: new Date().toISOString().substr(0, 7),
      }
    },
  }
</script>

```
