# Vuetify component v-timeline - usage

Example code

```vue
<template>
  <v-timeline>
    <v-timeline-item>timeline item</v-timeline-item>
    <v-timeline-item>
      timeline item
    </v-timeline-item>
    <v-timeline-item>timeline item</v-timeline-item>
  </v-timeline>
</template>

```

# Vuetify component v-timeline - slot icon

Example code

```vue
<template>
  <v-timeline>
    <v-timeline-item size="large">
      <template v-slot:icon>
        <v-avatar image="https://i.pravatar.cc/64"></v-avatar>
      </template>
      <template v-slot:opposite>
        <span>Tus eu perfecto</span>
      </template>
      <v-card class="elevation-2">
        <v-card-title class="text-h5">
          Lorem ipsum
        </v-card-title>
        <v-card-text>Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.</v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
</template>

```

# Vuetify component v-timeline - prop size

Example code

```vue
<template>
  <v-timeline>
    <v-timeline-item
      dot-color="purple-lighten-2"
      fill-dot
    >
      <v-card>
        <v-card-title class="bg-purple-lighten-2">
          <v-icon
            class="me-4"
            icon="mdi-magnify"
            size="large"
          ></v-icon>
          <h2 class="font-weight-light">
            Title 1
          </h2>
        </v-card-title>
        <v-card-text>
          Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit.
        </v-card-text>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      dot-color="amber-lighten-1"
      size="x-small"
      fill-dot
    >
      <v-card>
        <v-card-title class="bg-amber-lighten-1 justify-end">
          <h2 class="me-4 font-weight-light">
            Title 2
          </h2>
          <v-icon
            icon="mdi-home-outline"
            size="large"
          ></v-icon>
        </v-card-title>
        <v-card-text>
          Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit.
        </v-card-text>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      dot-color="cyan-lighten-1"
      fill-dot
    >
      <v-card>
        <v-card-title class="bg-cyan-lighten-1">
          <v-icon
            class="me-4"
            icon="mdi-email-outline"
            size="large"
          ></v-icon>
          <h2 class="font-weight-light">
            Title 3
          </h2>
        </v-card-title>
        <v-card-text>
          Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit.
        </v-card-text>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      dot-color="red-lighten-1"
      size="x-small"
      fill-dot
    >
      <v-card>
        <v-card-title class="bg-red-lighten-1 justify-end">
          <h2 class="me-4 font-weight-light">
            Title 4
          </h2>
          <v-icon
            icon="mdi-account-multiple-outline"
            size="large"
          ></v-icon>
        </v-card-title>
        <v-card-text>
          Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit.
        </v-card-text>
      </v-card>
    </v-timeline-item>

    <v-timeline-item
      dot-color="green-lighten-1"
      fill-dot
    >
      <v-card>
        <v-card-title class="bg-green-lighten-1">
          <v-icon
            class="me-4"
            icon="mdi-phone-in-talk"
            size="large"
          ></v-icon>
          <h2 class="font-weight-light">
            Title 5
          </h2>
        </v-card-title>
        <v-card-text>
          Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit.
        </v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
</template>

```

# Vuetify component v-timeline - slot opposite

Example code

```vue
<template>
  <v-timeline align="start">
    <v-timeline-item
      v-for="(year, i) in years"
      :key="i"
      :dot-color="year.color"
      size="small"
    >
      <template v-slot:opposite>
        <div
          :class="`pt-1 headline font-weight-bold text-${year.color}`"
          v-text="year.year"
        ></div>
      </template>
      <div>
        <h2 :class="`mt-n1 headline font-weight-light mb-4 text-${year.color}`">
          Lorem ipsum
        </h2>
        <div>
          Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.
        </div>
      </div>
    </v-timeline-item>
  </v-timeline>
</template>

<script setup>
  const years = [
    {
      color: 'cyan',
      year: '1960',
    },
    {
      color: 'green',
      year: '1970',
    },
    {
      color: 'pink',
      year: '1980',
    },
    {
      color: 'amber',
      year: '1990',
    },
    {
      color: 'orange',
      year: '2000',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      years: [
        {
          color: 'cyan',
          year: '1960',
        },
        {
          color: 'green',
          year: '1970',
        },
        {
          color: 'pink',
          year: '1980',
        },
        {
          color: 'amber',
          year: '1990',
        },
        {
          color: 'orange',
          year: '2000',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-timeline - prop truncate line

Example code

```vue
<template>
  <div class="d-flex justify-space-around">
    <v-timeline truncate-line="start">
      <v-timeline-item>
        <template v-slot:opposite>
          Opposite
        </template>
        Content
      </v-timeline-item>

      <v-timeline-item>
        <template v-slot:opposite>
          Opposite
        </template>
        Content
      </v-timeline-item>

      <v-timeline-item>
        <template v-slot:opposite>
          Opposite
        </template>
        Content
      </v-timeline-item>
    </v-timeline>

    <v-timeline truncate-line="end">
      <v-timeline-item>
        <template v-slot:opposite>
          Opposite
        </template>
        Content
      </v-timeline-item>

      <v-timeline-item>
        <template v-slot:opposite>
          Opposite
        </template>
        Content
      </v-timeline-item>

      <v-timeline-item>
        <template v-slot:opposite>
          Opposite
        </template>
        Content
      </v-timeline-item>
    </v-timeline>

    <v-timeline truncate-line="both">
      <v-timeline-item>
        <template v-slot:opposite>
          Opposite
        </template>
        Content
      </v-timeline-item>

      <v-timeline-item>
        <template v-slot:opposite>
          Opposite
        </template>
        Content
      </v-timeline-item>

      <v-timeline-item>
        <template v-slot:opposite>
          Opposite
        </template>
        Content
      </v-timeline-item>
    </v-timeline>
  </div>
</template>

```

# Vuetify component v-timeline - prop single side

Example code

```vue
<template>
  <v-timeline side="end">
    <v-timeline-item
      v-for="item in items"
      :key="item.id"
      :dot-color="item.color"
      size="small"
    >
      <v-alert
        :color="item.color"
        :icon="item.icon"
        :value="true"
      >
        Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.
      </v-alert>
    </v-timeline-item>
  </v-timeline>
</template>

<script setup>
  const items = [
    {
      id: 1,
      color: 'info',
      icon: 'mdi-information',
    },
    {
      id: 2,
      color: 'error',
      icon: 'mdi-alert-circle',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          id: 1,
          color: 'info',
          icon: 'mdi-information',
        },
        {
          id: 2,
          color: 'error',
          icon: 'mdi-alert-circle',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-timeline - prop direction

Example code

```vue
<template>
  <v-timeline direction="horizontal">
    <v-timeline-item>
      <template v-slot:opposite>
        Opposite content
      </template>
      <div>
        <div class="text-h6">Content title</div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>
    </v-timeline-item>

    <v-timeline-item>
      <template v-slot:opposite>
        Opposite content
      </template>
      <div>
        <div class="text-h6">Content title</div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>
    </v-timeline-item>

    <v-timeline-item>
      <template v-slot:opposite>
        Opposite content
      </template>
      <div>
        <div class="text-h6">Content title</div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>
    </v-timeline-item>
  </v-timeline>
</template>

```

# Vuetify component v-timeline - prop line inset

Example code

```vue
<template>
  <v-timeline direction="horizontal" line-inset="12">
    <v-timeline-item>
      <template v-slot:opposite>
        Opposite
      </template>
      Content
    </v-timeline-item>

    <v-timeline-item>
      <template v-slot:opposite>
        Opposite
      </template>
      Content
    </v-timeline-item>

    <v-timeline-item>
      <template v-slot:opposite>
        Opposite
      </template>
      Content
    </v-timeline-item>
  </v-timeline>
</template>

```

# Vuetify component v-timeline - prop color

Example code

```vue
<template>
  <v-timeline align="start" side="end">
    <v-timeline-item
      dot-color="pink"
      size="small"
    >
      <div class="d-flex">
        <strong class="me-4">5pm</strong>
        <div>
          <strong>New Icon</strong>
          <div class="text-caption">
            Mobile App
          </div>
        </div>
      </div>
    </v-timeline-item>

    <v-timeline-item
      dot-color="teal-lighten-3"
      size="small"
    >
      <div class="d-flex">
        <strong class="me-4">3-4pm</strong>
        <div>
          <strong>Design Stand Up</strong>
          <div class="text-caption mb-2">
            Hangouts
          </div>
        </div>
      </div>
    </v-timeline-item>

    <v-timeline-item
      dot-color="pink"
      size="small"
    >
      <div class="d-flex">
        <strong class="me-4">12pm</strong>
        <div>
          <strong>Lunch break</strong>
        </div>
      </div>
    </v-timeline-item>

    <v-timeline-item
      dot-color="teal-lighten-3"
      size="small"
    >
      <div class="d-flex">
        <strong class="me-4">9-11am</strong>
        <div>
          <strong>Finish Home Screen</strong>
          <div class="text-caption">
            Web App
          </div>
        </div>
      </div>
    </v-timeline-item>
  </v-timeline>
</template>

```

# Vuetify component v-timeline - prop mirror

Example code

```vue
<template>
  <div>
    <v-switch
      v-model="mirror"
      label="Toggle mirror"
    ></v-switch>
    <v-timeline
      :mirror="mirror"
    >
      <v-timeline-item
        v-for="n in 2"
        :key="n"
      >
        <template v-slot:opposite>
          <span>Tus eu perfecto</span>
        </template>
        <v-card class="elevation-2">
          <v-card-title class="text-h5">
            Lorem ipsum
          </v-card-title>
          <v-card-text>
            Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.
          </v-card-text>
        </v-card>
      </v-timeline-item>
    </v-timeline>
    <v-timeline
      :mirror="mirror"
      single-side="before"
    >
      <v-timeline-item
        v-for="n in 2"
        :key="n"
      >
        <template v-slot:opposite>
          <span>Tus eu perfecto</span>
        </template>
        <v-card class="elevation-2">
          <v-card-title class="text-h5">
            Lorem ipsum
          </v-card-title>
          <v-card-text>
            Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.
          </v-card-text>
        </v-card>
      </v-timeline-item>
    </v-timeline>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const mirror = ref(true)
</script>

<script>
  export default {
    data: () => ({
      mirror: true,
    }),
  }
</script>

```

# Vuetify component v-timeline - prop icon dots

Example code

```vue
<template>
  <v-timeline align="start">
    <v-timeline-item
      v-for="(item, i) in items"
      :key="i"
      :dot-color="item.color"
      :icon="item.icon"
      fill-dot
    >
      <v-card>
        <v-card-title :class="['text-h6', `bg-${item.color}`]">
          Lorem Ipsum Dolor
        </v-card-title>
        <v-card-text class="bg-white text--primary">
          <p>Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.</p>
          <v-btn
            :color="item.color"
            variant="outlined"
          >
            Button
          </v-btn>
        </v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
</template>

<script setup>
  const items = [
    {
      color: 'red-lighten-2',
      icon: 'mdi-star',
    },
    {
      color: 'purple-lighten-2',
      icon: 'mdi-book-variant',
    },
    {
      color: 'green-lighten-1',
      icon: 'mdi-airballoon',
    },
    {
      color: 'indigo-lighten-2',
      icon: 'mdi-layers-triple',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          color: 'red-lighten-2',
          icon: 'mdi-star',
        },
        {
          color: 'purple-lighten-2',
          icon: 'mdi-book-variant',
        },
        {
          color: 'green-lighten-1',
          icon: 'mdi-airballoon',
        },
        {
          color: 'indigo-lighten-2',
          icon: 'mdi-layers-triple',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-timeline - prop align

Example code

```vue
<template>
  <v-timeline align="start">
    <v-timeline-item>
      <template v-slot:opposite>
        Opposite content
      </template>
      <div>
        <div class="text-h6">Content title</div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>
    </v-timeline-item>

    <v-timeline-item>
      <template v-slot:opposite>
        Opposite content
      </template>
      <div>
        <div class="text-h6">Content title</div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>
    </v-timeline-item>

    <v-timeline-item>
      <template v-slot:opposite>
        Opposite content
      </template>
      <div>
        <div class="text-h6">Content title</div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>
    </v-timeline-item>
  </v-timeline>
</template>

```

# Vuetify component v-timeline - misc advanced

Example code

```vue
<template>
  <v-container style="max-width: 600px;">
    <v-timeline
      density="compact"
      side="end"
    >
      <v-timeline-item
        class="mb-12"
        dot-color="orange"
        size="large"
        fill-dot
      >
        <template v-slot:icon>
          <span>JL</span>
        </template>
        <v-text-field
          v-model="input"
          density="compact"
          label="Leave a comment..."
          hide-details
          @keydown.enter="comment"
        >
          <template v-slot:append>
            <v-btn
              class="mx-0"
              variant="text"
              @click="comment"
            >
              Post
            </v-btn>
          </template>
        </v-text-field>
      </v-timeline-item>

      <v-slide-x-transition group>
        <v-timeline-item
          v-for="event in timeline"
          :key="event.id"
          class="mb-4"
          dot-color="pink"
          size="small"
        >
          <div class="d-flex justify-space-between flex-grow-1">
            <div>{{ event.text }}</div>
            <div class="flex-shrink-0">{{ event.time }}</div>
          </div>
        </v-timeline-item>
      </v-slide-x-transition>

      <v-timeline-item
        class="mb-6"
        hide-dot
      >
        <span>TODAY</span>
      </v-timeline-item>

      <v-timeline-item
        class="mb-4"
        dot-color="grey"
        size="small"
      >
        <div class="d-flex justify-space-between flex-grow-1">
          <div>
            This order was archived.
          </div>
          <div class="flex-shrink-0">
            15:26 EDT
          </div>
        </div>
      </v-timeline-item>

      <v-timeline-item
        class="mb-4"
        dot-color="primary"
        size="small"
      >
        <div class="d-flex justify-space-between flex-grow-1">
          <div>
            <v-chip
              class="ms-0"
              color="purple"
              size="small"
              label
            >
              APP
            </v-chip>
            Digital Downloads fulfilled 1 item.
          </div>
          <div class="flex-shrink-0">
            15:25 EDT
          </div>
        </div>
      </v-timeline-item>

      <v-timeline-item
        class="mb-4"
        dot-color="grey"
        size="small"
      >
        <div class="d-flex justify-space-between flex-grow-1">
          <div>
            Order confirmation email was sent to John Leider (john@google.com).
          </div>
          <div class="flex-shrink-0">
            15:25 EDT
          </div>
        </div>
      </v-timeline-item>

      <v-timeline-item
        class="mb-4"
        hide-dot
      >
        <v-btn
          variant="outlined"
        >
          Resend Email
        </v-btn>
      </v-timeline-item>

      <v-timeline-item
        class="mb-4"
        dot-color="grey"
        size="small"
      >
        <div class="d-flex justify-space-between flex-grow-1">
          <div>
            A $15.00 USD payment was processed on PayPal Express Checkout
          </div>
          <div class="flex-shrink-0">
            15:25 EDT
          </div>
        </div>
      </v-timeline-item>

      <v-timeline-item
        dot-color="grey"
        size="small"
      >
        <div class="d-flex justify-space-between flex-grow-1">
          <div>
            John Leider placed this order on Online Store (checkout #1937432132572).
          </div>
          <div class="flex-shrink-0">
            15:25 EDT
          </div>
        </div>
      </v-timeline-item>
    </v-timeline>
  </v-container>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const events = ref([])
  const input = ref(null)
  const nonce = ref(0)

  const timeline = computed(() => {
    return events.value.slice().reverse()
  })

  function comment () {
    const time = (new Date()).toTimeString()
    events.value.push({
      id: nonce.value++,
      text: input.value,
      time: time.replace(/:\d{2}\sGMT-\d{4}\s\((.*)\)/, (match, contents, offset) => {
        return ` ${contents.split(' ').map(v => v.charAt(0)).join('')}`
      }),
    })
    input.value = null
  }
</script>

<script>
  export default {
    data: () => ({
      events: [],
      input: null,
      nonce: 0,
    }),

    computed: {
      timeline () {
        return this.events.slice().reverse()
      },
    },

    methods: {
      comment () {
        const time = (new Date()).toTimeString()
        this.events.push({
          id: this.nonce++,
          text: this.input,
          time: time.replace(/:\d{2}\sGMT-\d{4}\s\((.*)\)/, (match, contents, offset) => {
            return ` ${contents.split(' ').map(v => v.charAt(0)).join('')}`
          }),
        })

        this.input = null
      },
    },
  }
</script>

```
