# Vuetify component v-rating - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="selectedOption"
    :code="code"
    :name="name"
    :options="['Hearts']"
  >
    <div class="text-center">
      <v-rating v-bind="props"></v-rating>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="options['half-increments']" label="Half increments"></v-checkbox>
      <v-checkbox v-model="options.hover" label="Hover"></v-checkbox>
      <v-checkbox v-model="options.readonly" label="Readonly"></v-checkbox>

      <br>

      <v-slider v-model="options.length" :max="8" :min="1" label="Length"></v-slider>
      <v-slider v-model="options.size" :max="128" :min="16" label="Size"></v-slider>
      <v-slider v-model="options['model-value']" :max="options.length" :min="0" :step="options['half-increments'] ? 0.5 : 1" label="Value"></v-slider>

      <br>

      <v-select v-model="options.color" :items="colorOptions" label="Color"></v-select>
      <v-select v-model="options['active-color']" :items="colorOptions" label="Active color"></v-select>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const selectedOption = ref()

  const options = reactive({
    'half-increments': false,
    hover: true,
    readonly: false,

    length: 5,
    size: 32,
    'model-value': 3,

    color: null,
    'active-color': 'primary',
  })

  const name = 'v-rating'
  const props = computed(() => {
    return Object.fromEntries(
      Object.entries({
        ...options,
        ...(selectedOption.value === 'Hearts' ? {
          'empty-icon': 'mdi-heart-outline',
          'half-icon': 'mdi-heart-half-full',
          'full-icon': 'mdi-heart',
        } : undefined),
      }).filter(([key, value]) => value)
    )
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)} />`
  })

  const colorOptions = [
    'primary',
    'warning',
    'green',
    'red',
    'blue',
    'error',
    'teal',
    'red-lighten-3',
  ]
</script>

```

# Vuetify component v-rating - prop half increments

Example code

```vue
<template>
  <div class="text-center">
    <v-rating
      v-model="rating"
      half-increments
      hover
    ></v-rating>
    <pre>{{ rating }}</pre>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(3.5)
</script>

<script>
  export default {
    data: () => ({
      rating: 3.5,
    }),
  }
</script>

```

# Vuetify component v-rating - prop icon label

Example code

```vue
<template>
  <div class="text-center">
    <v-rating
      v-model="rating"
      item-aria-label="custom icon label text {0} of {1}"
    ></v-rating>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(4)
</script>

<script>
  export default {
    data: () => ({ rating: 4 }),
  }
</script>

```

# Vuetify component v-rating - prop size

Example code

```vue
<template>
  <div class="d-flex flex-column align-center">
    <v-rating
      model-value="3"
      size="x-small"
    ></v-rating>

    <v-rating
      model-value="3"
      size="small"
    ></v-rating>

    <v-rating
      model-value="3"
    ></v-rating>

    <v-rating
      model-value="3"
      size="large"
    ></v-rating>

    <v-rating
      model-value="3"
      size="x-large"
    ></v-rating>

    <v-rating
      model-value="3"
      size="72"
    ></v-rating>
  </div>
</template>

```

# Vuetify component v-rating - prop density

Example code

```vue
<template>
  <div class="d-flex flex-column align-center justify-center">
    <v-rating
      v-model="rating"
      class="ma-2"
      density="default"
    ></v-rating>

    <v-rating
      v-model="rating"
      class="ma-2"
      density="comfortable"
    ></v-rating>

    <v-rating
      v-model="rating"
      class="ma-2"
      density="compact"
    ></v-rating>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(3)
</script>

<script>
  export default {
    data: () => ({ rating: 3 }),
  }
</script>

```

# Vuetify component v-rating - slot item label

Example code

```vue
<template>
  <div class="text-center">
    <v-rating
      v-model="rating"
      :item-labels="labels"
    >
      <template v-slot:item-label="props">
        <span
          :class="`text-${colors[props.index]}`"
          class="font-weight-black text-caption"
        >
          {{ props.label }}
        </span>
      </template>
    </v-rating>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(4)
  const colors = ref(['red', 'orange', 'grey', 'cyan', 'green'])
  const labels = ref(['bad', 'so so', 'ok', 'good', 'great'])
</script>

<script>
  export default {
    data: () => ({
      rating: 4,
      colors: ['red', 'orange', 'grey', 'cyan', 'green'],
      labels: ['bad', 'so so', 'ok', 'good', 'great'],
    }),
  }
</script>

```

# Vuetify component v-rating - prop length

Example code

```vue
<template>
  <div class="text-center">
    <v-rating
      v-model="rating"
      length="10"
    ></v-rating>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(2)
</script>

<script>
  export default {
    data: () => ({
      rating: 2,
    }),
  }
</script>

```

# Vuetify component v-rating - prop clearable

Example code

```vue
<template>
  <div class="text-center">
    <v-rating
      v-model="rating"
      clearable
    ></v-rating>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(3)
</script>

<script>
  export default {
    data: () => ({
      rating: 3,
    }),
  }
</script>

```

# Vuetify component v-rating - prop icons

Example code

```vue
<template>
  <div class="text-center">
    <v-rating
      v-model="rating"
      empty-icon="mdi-circle-outline"
      full-icon="mdi-circle"
      half-increments
      hover
    ></v-rating>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(3.5)
</script>

<script>
  export default {
    data: () => ({
      rating: 3.5,
    }),
  }
</script>

```

# Vuetify component v-rating - prop readonly

Example code

```vue
<template>
  <div class="text-center">
    <v-rating
      v-model="rating"
      readonly
    ></v-rating>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(3)
</script>

<script>
  export default {
    data: () => ({
      rating: 3,
    }),
  }
</script>

```

# Vuetify component v-rating - prop item labels

Example code

```vue
<template>
  <div class="d-flex align-center justify-center flex-column">
    <v-rating
      v-model="rating"
      :item-labels="['sad', '', '', '', 'happy']"
      class="ma-2"
      item-label-position="top"
    ></v-rating>

    <v-rating
      v-model="rating"
      :item-labels="['sad', '', '', '', 'happy']"
      class="ma-2"
      item-label-position="bottom"
    ></v-rating>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(4)
</script>

<script>
  export default {
    data: () => ({ rating: 4 }),
  }
</script>

```

# Vuetify component v-rating - prop hover

Example code

```vue
<template>
  <div class="text-center">
    <v-rating
      v-model="rating"
      hover
    ></v-rating>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(3)
</script>

<script>
  export default {
    data: () => ({
      rating: 3,
    }),
  }
</script>

```

# Vuetify component v-rating - misc card

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    color="purple"
    elevation="10"
    width="360"
  >
    <div class="d-flex justify-between">
      <v-card-title class="flex-grow-1 flex-column align-start">
        <div class="text-h5">
          Halycon Days
        </div>
        <div class="text-h6 font-weight-thin">Ellie Goulding</div>

        <div class="text-h6 font-weight-thin">(2013)</div>
      </v-card-title>

      <v-img
        class="flex-grow-0"
        height="125px"
        src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"
        style="flex-basis: 125px"
      ></v-img>
    </div>

    <v-divider></v-divider>

    <v-card-actions class="pa-4">
      Rate this album

      <v-spacer></v-spacer>

      <span class="text-grey-lighten-2 text-caption me-2">
        ({{ rating }})
      </span>

      <v-rating
        v-model="rating"
        active-color="yellow-accent-4"
        color="white"
        size="18"
        half-increments
        hover
      ></v-rating>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(4.5)
</script>

<script>
  export default {
    data: () => ({ rating: 4.5 }),
  }
</script>

```

# Vuetify component v-rating - misc card overview

Example code

```vue
<template>
  <v-card
    class="d-flex flex-column mx-auto py-8"
    elevation="10"
    height="500"
    width="360"
  >
    <div class="d-flex justify-center mt-auto text-h5 ">
      Rating overview
    </div>

    <div class="d-flex align-center flex-column my-auto">
      <div class="text-h2 mt-5">
        3.5
        <span class="text-h6 ml-n3">/5</span>
      </div>

      <v-rating
        :model-value="3.5"
        color="yellow-darken-3"
        half-increments
      ></v-rating>
      <div class="px-3">3,360 ratings</div>
    </div>

    <v-list
      bg-color="transparent"
      class="d-flex flex-column-reverse"
      density="compact"
    >
      <v-list-item v-for="(rating,i) in 5" :key="i">
        <v-progress-linear
          :model-value="rating * 15"
          class="mx-n5"
          color="yellow-darken-3"
          height="20"
          rounded
        ></v-progress-linear>

        <template v-slot:prepend>
          <span>{{ rating }}</span>
          <v-icon class="mx-3" icon="mdi-star"></v-icon>
        </template>

        <template v-slot:append>
          <div class="rating-values">
            <span class="d-flex justify-end"> {{ rating * 224 }} </span>
          </div>
        </template>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<style>
.rating-values {
   width: 25px;
}
</style>

```

# Vuetify component v-rating - prop color

Example code

```vue
<template>
  <div class="text-center">
    <v-rating
      v-model="rating"
      active-color="blue"
      color="orange-lighten-1"
    ></v-rating>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const rating = ref(3)
</script>

<script>
  export default {
    data: () => ({ rating: 3 }),
  }
</script>

```

# Vuetify component v-rating - slot item

Example code

```vue
<template>
  <div class="text-center">
    <v-rating v-model="rating">
      <template v-slot:item="props">
        <v-icon
          :color="props.isFilled ? colors[props.index] : 'grey-lighten-1'"
          size="large"
        >
          {{ props.isFilled ? 'mdi-star-circle' : 'mdi-star-circle-outline' }}
        </v-icon>
      </template>
    </v-rating>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const colors = ['green', 'purple', 'orange', 'indigo', 'red']

  const rating = ref(4.5)
</script>

<script>
  export default {
    data: () => ({
      colors: ['green', 'purple', 'orange', 'indigo', 'red'],
      rating: 4.5,
    }),
  }
</script>

```

# Vuetify component v-rating - misc advanced

Example code

```vue
<template>
  <v-card
    class="mx-auto overflow-hidden"
    max-width="600"
  >
    <v-row>
      <v-col
        class="d-flex"
        cols="6"
      >
        <v-img src="https://cdn.vuetifyjs.com/images/ratings/fortnite1.png"></v-img>
      </v-col>

      <v-col cols="6">
        <v-container class="pa-0 ps-2 my-n1">
          <v-row>
            <v-col
              class="d-flex"
              cols="7"
            >
              <v-img src="https://cdn.vuetifyjs.com/images/ratings/fortnite2.png"></v-img>
            </v-col>

            <v-col
              class="d-flex"
              cols="5"
            >
              <v-img src="https://cdn.vuetifyjs.com/images/ratings/fortnite3.png"></v-img>
            </v-col>

            <v-col
              class="d-flex"
              cols="5"
            >
              <v-img src="https://cdn.vuetifyjs.com/images/ratings/fortnite4.png"></v-img>
            </v-col>

            <v-col
              class="d-flex"
              cols="7"
            >
              <v-img src="https://cdn.vuetifyjs.com/images/ratings/fortnite5.png"></v-img>
            </v-col>
          </v-row>
        </v-container>
      </v-col>
    </v-row>

    <v-card-title class="align-start">
      <div>
        <span class="text-h5">FORTNITE</span>
        <div class="text-grey font-weight-light">
          Video game
        </div>
      </div>

      <v-spacer></v-spacer>

      <v-dialog
        v-model="dialog"
        width="400"
      >
        <template v-slot:activator="{ props }">
          <v-icon v-bind="props" icon="mdi-share-variant"></v-icon>
        </template>

        <v-card>
          <v-card-title class="d-flex">
            <span class="text-h6 font-weight-bold">Share</span>
            <v-spacer></v-spacer>

            <v-btn class="mx-0" icon @click="dialog = false">
              <v-icon>mdi-close-circle-outline</v-icon>
            </v-btn>
          </v-card-title>

          <v-list>
            <v-list-item prepend-icon="mdi-facebook" title="Facebook"></v-list-item>
            <v-list-item prepend-icon="mdi-twitter" title="Twitter"></v-list-item>
            <v-list-item prepend-icon="mdi-email" title="Email"></v-list-item>
          </v-list>

          <v-text-field
            ref="link"
            :label="copied ? 'Link copied' : 'Click to copy link'"
            class="pa-4"
            model-value="https://g.co/kgs/nkrK43"
            readonly
            @click="copy"
          ></v-text-field>
        </v-card>
      </v-dialog>
    </v-card-title>

    <v-divider></v-divider>

    <v-card-actions>
      <span class="ps-2 text-grey-darken-2 font-weight-light text-caption">16,544 reviews</span>

      <v-spacer></v-spacer>

      <v-rating
        v-model="rating"
        length="10"
        readonly
      >
        <template v-slot:item="props">
          <v-icon
            :color="props.isFilled ? 'purple-darken-4' : ''"
            :icon="`mdi-numeric-${props.index}-box`"
            size="large"
          ></v-icon>
        </template>
      </v-rating>
    </v-card-actions>
    <div class="pa-4 pt-0 text-caption">
      <em>Portions of the materials used are trademarks and/or copyrighted works of Epic Games, Inc. All rights reserved by Epic. This material is not official and is not endorsed by Epic.</em>
    </div>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const link = ref()

  const copied = ref(false)
  const dialog = ref(false)
  const rating = ref(10)

  function copy () {
    link.value.focus()
    document.execCommand('selectAll', false, null)
    copied.value = document.execCommand('copy')
  }
</script>

<script>
  export default {
    data: () => ({
      copied: false,
      dialog: false,
      rating: 10,
    }),

    methods: {
      copy () {
        this.$refs.link.focus()

        document.execCommand('selectAll', false, null)

        this.copied = document.execCommand('copy')
      },
    },
  }
</script>

```
