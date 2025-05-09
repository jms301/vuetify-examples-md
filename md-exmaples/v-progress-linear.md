# Vuetify component v-progress-linear - usage

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
      <v-progress-linear v-bind="props"></v-progress-linear>
    </div>

    <template v-slot:configuration>
      <v-select
        v-model="color"
        :items="['primary', 'blue-lighten-3', 'error', 'blue-darken-3']"
        label="Color"
        clearable
      ></v-select>

      <v-slider
        v-model="height"
        label="Height"
        max="12"
        min="4"
        step="1"
      ></v-slider>

      <v-checkbox v-model="indeterminate" label="Indeterminate"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-progress-linear'
  const model = ref('default')
  const color = ref()
  const indeterminate = ref(false)
  const height = ref()
  const options = []
  const props = computed(() => {
    return {
      color: color.value || undefined,
      indeterminate: indeterminate.value || undefined,
      'model-value': !indeterminate.value ? '20' : undefined,
      height: height.value !== 4 ? height.value : undefined,
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

# Vuetify component v-progress-linear - prop rounded

Example code

```vue
<template>
  <div>
    <v-progress-linear
      color="red-darken-2"
      model-value="100"
      rounded
    ></v-progress-linear>
    <br>
    <v-progress-linear
      color="indigo"
      model-value="100"
      rounded
    ></v-progress-linear>
    <br>
    <v-progress-linear
      color="teal"
      model-value="100"
      rounded
    ></v-progress-linear>
    <br>
    <v-progress-linear
      color="cyan-darken-2"
      model-value="100"
      rounded
    ></v-progress-linear>
  </div>
</template>

```

# Vuetify component v-progress-linear - prop indeterminate

Example code

```vue
<template>
  <div>
    <v-progress-linear
      color="yellow-darken-2"
      indeterminate
    ></v-progress-linear>
    <br>
    <v-progress-linear
      color="green"
      indeterminate
    ></v-progress-linear>
    <br>
    <v-progress-linear
      color="teal"
      indeterminate
    ></v-progress-linear>
    <br>
    <v-progress-linear
      color="cyan"
      indeterminate
    ></v-progress-linear>
  </div>
</template>

```

# Vuetify component v-progress-linear - misc determinate

Example code

```vue
<template>
  <div>
    <v-progress-linear
      v-model="valueDeterminate"
      color="deep-purple-accent-4"
    ></v-progress-linear>
    <br>
    <v-progress-linear
      v-model="valueDeterminate"
      color="pink"
    ></v-progress-linear>
    <br>
    <v-progress-linear
      v-model="valueDeterminate"
      color="indigo-darken-2"
    ></v-progress-linear>
    <br>
    <v-progress-linear
      v-model="valueDeterminate"
      color="amber"
    ></v-progress-linear>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const valueDeterminate = ref(50)
</script>

<script>
  export default {
    data () {
      return {
        valueDeterminate: 50,
      }
    },
  }
</script>

```

# Vuetify component v-progress-linear - prop reverse

Example code

```vue
<template>
  <div>
    <v-progress-linear
      color="pink"
      model-value="15"
      reverse
    ></v-progress-linear>

    <br>

    <v-progress-linear
      color="lime"
      indeterminate
      reverse
    ></v-progress-linear>

    <br>

    <v-progress-linear
      buffer-value="55"
      color="success"
      model-value="30"
      reverse
      streams
    ></v-progress-linear>

    <br>

    <p>In specific cases you may want progress to display in left-to-right mode regardless of the application direction (LTR or RTL):</p>

    <v-progress-linear
      :reverse="$vuetify.locale.isRtl"
      model-value="15"
    ></v-progress-linear>
  </div>
</template>

```

# Vuetify component v-progress-linear - misc file loader

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-toolbar color="deep-purple-accent-4">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>My Files</v-toolbar-title>

      <v-btn
        color="white"
        location="bottom left"
        absolute
        icon
      >
        <v-icon>mdi-plus</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-share-variant</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>

    <v-container style="height: 400px;">
      <v-row
        align-content="center"
        class="fill-height"
        justify="center"
      >
        <v-col
          class="text-subtitle-1 text-center"
          cols="12"
        >
          Getting your files
        </v-col>
        <v-col cols="6">
          <v-progress-linear
            color="deep-purple-accent-4"
            height="6"
            indeterminate
            rounded
          ></v-progress-linear>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

```

# Vuetify component v-progress-linear - prop stream

Example code

```vue
<template>
  <div>
    <v-progress-linear
      buffer-value="0"
      color="red-lighten-2"
      stream
    ></v-progress-linear>
    <br>
    <v-progress-linear
      buffer-value="0"
      color="teal"
      model-value="20"
      stream
    ></v-progress-linear>
    <br>
    <v-progress-linear
      buffer-value="50"
      color="cyan"
      stream
    ></v-progress-linear>
    <br>
    <v-progress-linear
      buffer-value="60"
      color="orange"
      model-value="40"
      stream
    ></v-progress-linear>
  </div>
</template>

```

# Vuetify component v-progress-linear - prop query

Example code

```vue
<template>
  <div style="min-height: 4px;">
    <v-progress-linear
      v-model="value"
      :active="show"
      :indeterminate="query"
      :query="true"
    ></v-progress-linear>
  </div>
</template>

<script setup>
  import { onBeforeUnmount, onMounted, ref } from 'vue'

  const value = ref(0)
  const query = ref(false)
  const show = ref(true)

  let interval = -1
  onMounted(() => {
    queryAndIndeterminate()
  })
  onBeforeUnmount(() => {
    clearInterval(interval)
  })

  function queryAndIndeterminate () {
    query.value = true
    show.value = true
    value.value = 0
    setTimeout(() => {
      query.value = false
      interval = setInterval(() => {
        if (value.value === 100) {
          clearInterval(interval)
          show.value = false
          return setTimeout(queryAndIndeterminate, 2000)
        }
        value.value += 25
      }, 1000)
    }, 2500)
  }
</script>

<script>
  export default {
    data () {
      return {
        value: 0,
        query: false,
        show: true,
        interval: 0,
      }
    },

    mounted () {
      this.queryAndIndeterminate()
    },

    beforeUnmount () {
      clearInterval(this.interval)
    },

    methods: {
      queryAndIndeterminate () {
        this.query = true
        this.show = true
        this.value = 0

        setTimeout(() => {
          this.query = false

          this.interval = setInterval(() => {
            if (this.value === 100) {
              clearInterval(this.interval)
              this.show = false
              return setTimeout(this.queryAndIndeterminate, 2000)
            }
            this.value += 25
          }, 1000)
        }, 2500)
      },
    },
  }
</script>

```

# Vuetify component v-progress-linear - slot default

Example code

```vue
<template>
  <div>
    <v-progress-linear
      v-model="power"
      color="amber"
      height="25"
    ></v-progress-linear>

    <br>

    <v-progress-linear
      v-model="skill"
      color="blue-grey"
      height="25"
    >
      <template v-slot:default="{ value }">
        <strong>{{ Math.ceil(value) }}%</strong>
      </template>
    </v-progress-linear>

    <br>

    <v-progress-linear
      v-model="knowledge"
      height="25"
    >
      <strong>{{ Math.ceil(knowledge) }}%</strong>
    </v-progress-linear>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const skill = ref(20)
  const knowledge = ref(33)
  const power = ref(78)
</script>

<script>
  export default {
    data: () => ({
      skill: 20,
      knowledge: 33,
      power: 78,
    }),
  }
</script>

```

# Vuetify component v-progress-linear - prop buffer value

Example code

```vue
<template>
  <div>
    <v-progress-linear
      v-model="value"
      :buffer-value="bufferValue"
    ></v-progress-linear>
    <br>
    <v-progress-linear
      v-model="value"
      :buffer-value="bufferValue"
      color="purple"
    ></v-progress-linear>
    <br>
    <v-progress-linear
      v-model="value"
      :buffer-value="bufferValue"
      color="red-lighten-2"
    ></v-progress-linear>
    <br>
    <v-progress-linear
      v-model="value"
      :buffer-value="bufferValue"
      color="black"
    ></v-progress-linear>
  </div>
</template>

<script setup>
  import { onBeforeUnmount, onMounted, ref, watch } from 'vue'

  const value = ref(10)
  const bufferValue = ref(20)
  const interval = ref(0)

  watch(value, val => {
    if (val < 100) return
    value.value = 0
    bufferValue.value = 10
    startBuffer()
  })

  onMounted(() => {
    startBuffer()
  })
  onBeforeUnmount(() => {
    clearInterval(interval.value)
  })

  function startBuffer () {
    clearInterval(interval.value)
    interval.value = setInterval(() => {
      value.value += Math.random() * (15 - 5) + 5
      bufferValue.value += Math.random() * (15 - 5) + 6
    }, 2000)
  }
</script>

<script>
  export default {
    data () {
      return {
        value: 10,
        bufferValue: 20,
        interval: 0,
      }
    },

    watch: {
      value (val) {
        if (val < 100) return

        this.value = 0
        this.bufferValue = 10
        this.startBuffer()
      },
    },

    mounted () {
      this.startBuffer()
    },

    beforeUnmount () {
      clearInterval(this.interval)
    },

    methods: {
      startBuffer () {
        clearInterval(this.interval)

        this.interval = setInterval(() => {
          this.value += Math.random() * (15 - 5) + 5
          this.bufferValue += Math.random() * (15 - 5) + 6
        }, 2000)
      },
    },
  }
</script>

```

# Vuetify component v-progress-linear - prop striped

Example code

```vue
<template>
  <div>
    <v-progress-linear
      color="light-blue"
      height="10"
      model-value="10"
      striped
    ></v-progress-linear>
    <br>
    <v-progress-linear
      color="light-green-darken-4"
      height="10"
      model-value="20"
      striped
    ></v-progress-linear>
    <br>
    <v-progress-linear
      color="lime"
      height="10"
      model-value="45"
      striped
    ></v-progress-linear>
    <br>
    <v-progress-linear
      color="deep-orange"
      height="10"
      model-value="60"
      striped
    ></v-progress-linear>
  </div>
</template>

```

# Vuetify component v-progress-linear - misc buffer color

Example code

```vue
<template>
  <v-sheet
    class="d-flex align-center px-4 py-8 mx-auto"
    color="#181a1b"
    max-width="250"
    rounded="lg"
  >
    <v-progress-linear
      :location="null"
      bg-color="#92aed9"
      buffer-color="#6a3e0b"
      buffer-opacity="1"
      buffer-value="3"
      color="#12512a"
      height="12"
      max="9"
      min="0"
      model-value="2"
      rounded
    ></v-progress-linear>

    <div class="ms-4 text-h6">3/9</div>
  </v-sheet>
</template>

```

# Vuetify component v-progress-linear - prop colors

Example code

```vue
<template>
  <div>
    <v-progress-linear
      bg-color="pink-lighten-3"
      color="pink-lighten-1"
      model-value="15"
    ></v-progress-linear>
    <br>
    <v-progress-linear
      bg-color="blue-grey"
      color="lime"
      model-value="30"
    ></v-progress-linear>
    <br>
    <v-progress-linear
      bg-color="success"
      color="error"
      model-value="45"
    ></v-progress-linear>
  </div>
</template>

```

# Vuetify component v-progress-linear - misc toolbar loader

Example code

```vue
<template>
  <v-card
    class="mx-auto mt-6"
    width="344"
  >
    <v-toolbar>
      <v-btn icon>
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>

      <v-toolbar-title>My Recipes</v-toolbar-title>

      <v-progress-linear
        :active="loading"
        :indeterminate="loading"
        color="deep-purple-accent-4"
        location="bottom"
        absolute
      ></v-progress-linear>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>

    <v-container style="height: 282px;">
      <v-row
        align="center"
        class="fill-height"
        justify="center"
      >
        <v-scale-transition>
          <div
            v-if="!loading"
            class="text-center"
          >
            <v-btn
              color="primary"
              @click="loading = true"
            >
              Start loading
            </v-btn>
          </div>
        </v-scale-transition>
      </v-row>
    </v-container>
  </v-card>
</template>

<script setup>
  import { ref, watch } from 'vue'

  const loading = ref(false)

  watch(loading, val => {
    if (!val) return
    setTimeout(() => (loading.value = false), 3000)
  })
</script>

<script>
  export default {
    data: () => ({
      loading: false,
    }),

    watch: {
      loading (val) {
        if (!val) return

        setTimeout(() => (this.loading = false), 3000)
      },
    },
  }
</script>

```
