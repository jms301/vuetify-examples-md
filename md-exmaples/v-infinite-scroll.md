# Vuetify component v-infinite-scroll - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
    :script="script"
  >
    <div>
      <v-infinite-scroll
        v-bind="props"
        :items="items.value"
        @load="load"
      >
        <template v-for="(item, index) in items" :key="item">
          <div :class="['pa-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
            Item number {{ item }}
          </div>
        </template>
      </v-infinite-scroll>
    </div>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-infinite-scroll'
  const model = ref('default')
  const options = []
  const items = ref(Array.from({ length: 30 }, (k, v) => v + 1))

  function api () {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve(Array.from({ length: 10 }, (k, v) => v + items.value.at(-1) + 1))
      }, 1000)
    })
  }

  async function load ({ done }) {
    // Perform API call
    const res = await api()

    items.value.push(...res)

    done('ok')
  }

  const props = computed(() => {
    return {
      height: 300,
      items: 'items',
      onLoad: 'load',
    }
  })

  const slots = computed(() => {
    return `
  <template v-for="(item, index) in items" :key="item">
    <div :class="['pa-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
      Item number #{{ item }}
    </div>
  </template>
`
  })

  const code = computed(() => {
    return `<v-infinite-scroll${propsToString(props.value, ['items'])}>${slots.value}</v-infinite-scroll>`
  })

  const script = computed(() => {
    return `<script setup>
  import { ref } from 'vue'

  const items = ref(Array.from({ length: 30 }, (k, v) => v + 1))

  async function api () {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve(Array.from({ length: 10 }, (k, v) => v + items.value.at(-1) + 1))
      }, 1000)
    })
  }
  async function load ({ done }) {
    // Perform API call
    const res = await api()

    items.value.push(...res)

    done('ok')
  }
<` + '/script>'
  })
</script>

```

# Vuetify component v-infinite-scroll - slot loading

Example code

```vue
<template>
  <v-infinite-scroll
    height="400"
    @load="load"
  >
    <template v-for="(item, index) in items" :key="item">
      <div :class="['pa-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
        Item #{{ item }}
      </div>
    </template>
    <template v-slot:loading>
      This is taking a very long time...
    </template>
  </v-infinite-scroll>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref(Array.from({ length: 50 }, (k, v) => v + 1))
  function load ({ done }) {
    setTimeout(() => {
      items.value.push(...Array.from({ length: 10 }, (k, v) => v + items.value.at(-1) + 1))
      done('ok')
    }, 4000)
  }
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 50 }, (k, v) => v + 1),
    }),

    methods: {
      load ({ done }) {
        setTimeout(() => {
          this.items.push(...Array.from({ length: 10 }, (k, v) => v + this.items.at(-1) + 1))

          done('ok')
        }, 4000)
      },
    },
  }
</script>

```

# Vuetify component v-infinite-scroll - slot empty

Example code

```vue
<template>
  <v-infinite-scroll
    height="400"
    @load="load"
  >
    <template v-for="(item, index) in items" :key="item">
      <div :class="['pa-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
        Item #{{ item }}
      </div>
    </template>
    <template v-slot:empty>
      <v-alert type="warning">No more items!</v-alert>
    </template>
  </v-infinite-scroll>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref(Array.from({ length: 50 }, (k, v) => v + 1))
  function load ({ done }) {
    setTimeout(() => {
      done('empty')
    }, 1000)
  }
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 50 }, (k, v) => v + 1),
    }),

    methods: {
      load ({ done }) {
        setTimeout(() => {
          done('empty')
        }, 1000)
      },
    },
  }
</script>

```

# Vuetify component v-infinite-scroll - prop side both

Example code

```vue
<template>
  <v-infinite-scroll
    height="300"
    side="both"
    @load="load"
  >
    <template v-for="(item, index) in items" :key="item">
      <div :class="['px-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
        Item number {{ item }}
      </div>
    </template>
  </v-infinite-scroll>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref(Array.from({ length: 50 }, (k, v) => v + 1))
  function load ({ side, done }) {
    setTimeout(() => {
      if (side === 'start') {
        const arr = Array.from({ length: 10 }, (k, v) => items.value[0] - (10 - v))
        items.value = [...arr, ...items.value]
      } else if (side === 'end') {
        const arr = Array.from({ length: 10 }, (k, v) => items.value.at(-1) + 1 + v)
        items.value = [...items.value, ...arr]
      }
      done('ok')
    }, 1000)
  }
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 50 }, (k, v) => v + 1),
    }),

    methods: {
      load ({ side, done }) {
        setTimeout(() => {
          if (side === 'start') {
            const arr = Array.from({ length: 10 }, (k, v) => this.items[0] - (10 - v))
            this.items = [...arr, ...this.items]
          } else if (side === 'end') {
            const arr = Array.from({ length: 10 }, (k, v) => this.items.at(-1) + 1 + v)
            this.items = [...this.items, ...arr]
          }

          done('ok')
        }, 1000)
      },
    },
  }
</script>

```

# Vuetify component v-infinite-scroll - slot load more

Example code

```vue
<template>
  <v-infinite-scroll
    height="400"
    mode="manual"
    @load="load"
  >
    <template v-for="(item, index) in items" :key="item">
      <div :class="['pa-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
        Item #{{ item }}
      </div>
    </template>
    <template v-slot:load-more="{ props }">
      <v-btn
        icon="mdi-refresh"
        size="small"
        variant="text"
        v-bind="props"
      ></v-btn>
    </template>
  </v-infinite-scroll>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref(Array.from({ length: 50 }, (k, v) => v + 1))
  function load ({ done }) {
    setTimeout(() => {
      items.value.push(...Array.from({ length: 10 }, (k, v) => v + items.value.at(-1) + 1))
      done('ok')
    }, 1000)
  }
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 50 }, (k, v) => v + 1),
    }),

    methods: {
      load ({ done }) {
        setTimeout(() => {
          this.items.push(...Array.from({ length: 10 }, (k, v) => v + this.items.at(-1) + 1))

          done('ok')
        }, 1000)
      },
    },
  }
</script>

```

# Vuetify component v-infinite-scroll - slot error

Example code

```vue
<template>
  <v-infinite-scroll
    height="400"
    @load="load"
  >
    <template v-for="(item, index) in items" :key="item">
      <div :class="['pa-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
        Item #{{ item }}
      </div>
    </template>
    <template v-slot:error="{ props }">
      <v-alert type="error">
        <div class="d-flex justify-space-between align-center">
          Something went wrong...
          <v-btn
            color="white"
            size="small"
            variant="outlined"
            v-bind="props"
          >
            Retry
          </v-btn>
        </div>
      </v-alert>
    </template>
  </v-infinite-scroll>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref(Array.from({ length: 50 }, (k, v) => v + 1))
  function load ({ done }) {
    setTimeout(() => {
      done('error')
    }, 2000)
  }
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 50 }, (k, v) => v + 1),
    }),

    methods: {
      load ({ done }) {
        setTimeout(() => {
          done('error')
        }, 2000)
      },
    },
  }
</script>

```

# Vuetify component v-infinite-scroll - prop direction

Example code

```vue
<template>
  <v-infinite-scroll
    direction="horizontal"
    @load="load"
  >
    <template v-for="(item, index) in items" :key="item">
      <div :class="['pa-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
        Item #{{ item }}
      </div>
    </template>
  </v-infinite-scroll>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref(Array.from({ length: 50 }, (k, v) => v + 1))

  function load ({ done }) {
    setTimeout(() => {
      items.value.push(...Array.from({ length: 10 }, (k, v) => v + items.value.at(-1) + 1))
      done('ok')
    }, 1000)
  }
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 50 }, (k, v) => v + 1),
    }),

    methods: {
      load ({ done }) {
        setTimeout(() => {
          this.items.push(...Array.from({ length: 10 }, (k, v) => v + this.items.at(-1) + 1))

          done('ok')
        }, 1000)
      },
    },
  }
</script>

```

# Vuetify component v-infinite-scroll - prop mode

Example code

```vue
<template>
  <v-infinite-scroll
    height="300"
    mode="manual"
    @load="load"
  >
    <template v-for="(item, index) in items" :key="item">
      <div :class="['px-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
        Item number {{ item }}
      </div>
    </template>
  </v-infinite-scroll>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref(Array.from({ length: 50 }, (k, v) => v + 1))
  function load ({ done }) {
    setTimeout(() => {
      items.value.push(...Array.from({ length: 10 }, (k, v) => v + items.value.at(-1) + 1))
      done('ok')
    }, 1000)
  }
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 50 }, (k, v) => v + 1),
    }),

    methods: {
      load ({ done }) {
        setTimeout(() => {
          this.items.push(...Array.from({ length: 10 }, (k, v) => v + this.items.at(-1) + 1))

          done('ok')
        }, 1000)
      },
    },
  }
</script>

```

# Vuetify component v-infinite-scroll - misc virtual

Example code

```vue
<template>
  <v-infinite-scroll
    ref="infinite"
    height="500"
    side="both"
    @load="load"
  >
    <div>
      <template v-for="card in cards" :key="card">
        <v-sheet
          :color="card % 2 === 0 ? 'primary' : card % 4 === 0 ? 'secondary' : 'warning'"
          :height="size"
          class="d-flex align-center justify-center"
        >
          <div>{{ card }}</div>
        </v-sheet>
      </template>
    </div>
  </v-infinite-scroll>
</template>

<script setup>
  import { nextTick, ref } from 'vue'

  const infinite = ref()

  const size = ref(300)
  const virtualLength = ref(12)
  const cards = ref([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

  function createRange (length, start) {
    return Array.from({ length }).map((_, i) => i + start)
  }
  function load ({ side, done }) {
    const halfVirtualLength = virtualLength.value / 2
    if (side === 'start') {
      const arr = createRange(halfVirtualLength, cards.value[0] - halfVirtualLength)
      cards.value = [...arr, ...cards.value.slice(0, halfVirtualLength)]
      nextTick(() => {
        infinite.value.$el.scrollTop = infinite.value.$el.scrollHeight - (halfVirtualLength * size.value) - infinite.value.$el.scrollTop
      })
    } else {
      const arr = createRange(halfVirtualLength, cards.value.at(-1) + 1)
      cards.value = [...cards.value.slice(halfVirtualLength), ...arr]
    }
    done('ok')
  }
</script>

<script>
  export default {
    data: () => ({
      size: 300,
      virtualLength: 12,
      cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    }),

    methods: {
      createRange (length, start) {
        return Array.from({ length }).map((_, i) => i + start)
      },
      load ({ side, done }) {
        const halfVirtualLength = this.virtualLength / 2
        if (side === 'start') {
          const arr = this.createRange(halfVirtualLength, this.cards[0] - halfVirtualLength)
          this.cards = [...arr, ...this.cards.slice(0, halfVirtualLength)]
          this.$nextTick(() => {
            this.$refs.infinite.$el.scrollTop = this.$refs.infinite.$el.scrollHeight - (halfVirtualLength * this.size) - this.$refs.infinite.$el.scrollTop
          })
        } else {
          const arr = this.createRange(halfVirtualLength, this.cards.at(-1) + 1)
          this.cards = [...this.cards.slice(halfVirtualLength), ...arr]
        }

        done('ok')
      },
    },
  }
</script>

```

# Vuetify component v-infinite-scroll - prop color

Example code

```vue
<template>
  <v-infinite-scroll
    color="secondary"
    height="400"
    mode="manual"
    @load="load"
  >
    <template v-for="(item, index) in items" :key="item">
      <div :class="['pa-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
        Item #{{ item }}
      </div>
    </template>
  </v-infinite-scroll>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref(Array.from({ length: 50 }, (k, v) => v + 1))

  function load ({ done }) {
    setTimeout(() => {
      items.value.push(...Array.from({ length: 10 }, (k, v) => v + items.value.at(-1) + 1))
      done('ok')
    }, 1000)
  }
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 50 }, (k, v) => v + 1),
    }),

    methods: {
      load ({ done }) {
        setTimeout(() => {
          this.items.push(...Array.from({ length: 10 }, (k, v) => v + this.items.at(-1) + 1))

          done('ok')
        }, 1000)
      },
    },
  }
</script>

```

# Vuetify component v-infinite-scroll - prop side start

Example code

```vue
<template>
  <v-infinite-scroll
    height="300"
    side="start"
    @load="load"
  >
    <template v-for="(item, index) in items" :key="item">
      <div :class="['px-2', index % 2 === 0 ? 'bg-grey-lighten-2' : '']">
        Item number {{ item }}
      </div>
    </template>
  </v-infinite-scroll>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ref(Array.from({ length: 50 }, (k, v) => v + 1))
  function load ({ done }) {
    setTimeout(() => {
      items.value.unshift(...Array.from({ length: 10 }, (k, v) => items.value[0] - (10 - v)))
      done('ok')
    }, 1000)
  }
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 50 }, (k, v) => v + 1),
    }),

    methods: {
      load ({ done }) {
        setTimeout(() => {
          this.items.unshift(...Array.from({ length: 10 }, (k, v) => this.items[0] - (10 - v)))

          done('ok')
        }, 1000)
      },
    },
  }
</script>

```
