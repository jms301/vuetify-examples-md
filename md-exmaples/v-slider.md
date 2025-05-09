# Vuetify component v-slider - usage

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
      <v-slider v-bind="props"></v-slider>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="disabled" label="Disabled"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-slider'
  const model = ref('default')
  const options = ['vertical']
  const disabled = ref(false)
  const props = computed(() => {
    return {
      direction: model.value === 'vertical' ? 'vertical' : undefined,
      disabled: disabled.value || undefined,
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

# Vuetify component v-slider - prop validation

Example code

```vue
<template>
  <v-card
    color="transparent"
    flat
  >
    <div class="text-subtitle-2">Rules</div>

    <v-card-text class="pt-0">
      <v-slider
        v-model="value"
        :rules="rules"
        label="How many?"
        step="10"
        thumb-label="always"
        ticks
      ></v-slider>
    </v-card-text>

    <div class="text-subtitle-2">Persistent hint</div>

    <v-card-text class="pt-0">
      <v-slider
        v-model="value"
        :rules="rules"
        hint="40 in stock"
        label="How many?"
        step="10"
        thumb-label="always"
        persistent-hint
        ticks
      ></v-slider>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref(30)

  const rules = [
    v => v <= 40 || 'Only 40 in stock',
  ]
</script>

<script>
  export default {
    data () {
      return {
        value: 30,
        rules: [
          v => v <= 40 || 'Only 40 in stock',
        ],
      }
    },
  }
</script>

```

# Vuetify component v-slider - slot append text field

Example code

```vue
<template>
  <v-card style="margin: auto" width="400">
    <v-responsive
      :style="{ background: `rgb(${red}, ${green}, ${blue})` }"
      height="300px"
    ></v-responsive>

    <v-card-text>
      <v-slider
        v-model="red"
        :max="255"
        :step="1"
        class="ma-4"
        label="R"
        hide-details
      >
        <template v-slot:append>
          <v-text-field
            v-model="red"
            density="compact"
            style="width: 80px"
            type="number"
            variant="outlined"
            hide-details
          ></v-text-field>
        </template>
      </v-slider>

      <v-slider
        v-model="green"
        :max="255"
        :step="1"
        class="ma-4"
        label="G"
        hide-details
      >
        <template v-slot:append>
          <v-text-field
            v-model="green"
            density="compact"
            style="width: 80px"
            type="number"
            variant="outlined"
            hide-details
          ></v-text-field>
        </template>
      </v-slider>

      <v-slider
        v-model="blue"
        :max="255"
        :step="1"
        class="ma-4"
        label="B"
        hide-details
      >
        <template v-slot:append>
          <v-text-field
            v-model="blue"
            density="compact"
            style="width: 80px"
            type="number"
            variant="outlined"
            hide-details
          ></v-text-field>
        </template>
      </v-slider>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const red = ref(64)
  const green = ref(128)
  const blue = ref(10)
</script>

<script>
  export default {
    data () {
      return {
        red: 64,
        green: 128,
        blue: 10,
      }
    },
  }
</script>

```

# Vuetify component v-slider - slot append and prepend

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="600"
  >
    <v-toolbar
      dense
      flat
    >
      <v-toolbar-title>
        <span class="text-subheading">METRONOME</span>
      </v-toolbar-title>
      <v-btn icon="mdi-share-variant" variant="text"></v-btn>
    </v-toolbar>

    <v-card-text>
      <v-row
        class="mb-4"
        justify="space-between"
      >
        <v-col class="text-left">
          <span
            class="text-h2 font-weight-light"
            v-text="bpm"
          ></span>
          <span class="subheading font-weight-light me-1">BPM</span>
          <v-fade-transition>
            <v-avatar
              v-if="isPlaying"
              :color="color"
              :style="{
                animationDuration: animationDuration
              }"
              class="mb-1 v-avatar--metronome"
              size="12"
            ></v-avatar>
          </v-fade-transition>
        </v-col>
        <v-col class="text-right">
          <v-btn
            :color="color"
            elevation="0"
            theme="dark"
            icon
            @click="toggle"
          >
            <v-icon :icon="isPlaying ? 'mdi-pause' : 'mdi-play'" size="large"></v-icon>
          </v-btn>
        </v-col>
      </v-row>

      <v-slider
        v-model="bpm"
        :color="color"
        :step="1"
        max="218"
        min="40"
        track-color="grey"
      >
        <template v-slot:prepend>
          <v-btn
            :color="color"
            icon="mdi-minus"
            size="small"
            variant="text"
            @click="decrement"
          ></v-btn>
        </template>

        <template v-slot:append>
          <v-btn
            :color="color"
            icon="mdi-plus"
            size="small"
            variant="text"
            @click="increment"
          ></v-btn>
        </template>
      </v-slider>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const bpm = ref(40)
  const isPlaying = ref(false)

  const color = computed(() => {
    if (bpm.value < 100) return 'indigo'
    if (bpm.value < 125) return 'teal'
    if (bpm.value < 140) return 'green'
    if (bpm.value < 175) return 'orange'
    return 'red'
  })
  const animationDuration = computed(() => {
    return `${60 / bpm.value}s`
  })

  function decrement () {
    bpm.value--
  }
  function increment () {
    bpm.value++
  }
  function toggle () {
    isPlaying.value = !isPlaying.value
  }
</script>

<script>
  export default {
    data: () => ({
      bpm: 40,
      isPlaying: false,
    }),

    computed: {
      color () {
        if (this.bpm < 100) return 'indigo'
        if (this.bpm < 125) return 'teal'
        if (this.bpm < 140) return 'green'
        if (this.bpm < 175) return 'orange'
        return 'red'
      },
      animationDuration () {
        return `${60 / this.bpm}s`
      },
    },

    methods: {
      decrement () {
        this.bpm--
      },
      increment () {
        this.bpm++
      },
      toggle () {
        this.isPlaying = !this.isPlaying
      },
    },
  }
</script>

<style>
  @keyframes metronome-example {
    from {
      transform: scale(.5);
    }

    to {
      transform: scale(1);
    }
  }

  .v-avatar--metronome {
    animation-name: metronome-example;
    animation-iteration-count: infinite;
    animation-direction: alternate;
  }
</style>

```

# Vuetify component v-slider - prop ticks

Example code

```vue
<template>
  <div>
    <div class="text-caption">Show ticks when using slider</div>

    <v-slider
      step="10"
      show-ticks
    ></v-slider>

    <div class="text-caption">Always show ticks</div>

    <v-slider
      show-ticks="always"
      step="10"
    ></v-slider>

    <div class="text-caption">Tick size</div>

    <v-slider
      show-ticks="always"
      step="10"
      tick-size="4"
    ></v-slider>

    <div class="text-caption">Tick labels</div>

    <v-slider
      :max="3"
      :ticks="tickLabels"
      show-ticks="always"
      step="1"
      tick-size="4"
    ></v-slider>
  </div>
</template>

<script setup>
  const tickLabels = {
    0: 'Figs',
    1: 'Lemon',
    2: 'Pear',
    3: 'Apple',
  }
</script>

<script>
  export default {
    data () {
      return {
        tickLabels: {
          0: 'Figs',
          1: 'Lemon',
          2: 'Pear',
          3: 'Apple',
        },
      }
    },
  }
</script>

```

# Vuetify component v-slider - prop min and max

Example code

```vue
<template>
  <v-slider
    v-model="slider"
    :max="max"
    :min="min"
    class="align-center"
    hide-details
  >
    <template v-slot:append>
      <v-text-field
        v-model="slider"
        density="compact"
        style="width: 70px"
        type="number"
        hide-details
        single-line
      ></v-text-field>
    </template>
  </v-slider>
</template>

<script setup>
  import { ref } from 'vue'

  const min = ref(-50)
  const max = ref(90)
  const slider = ref(40)
</script>

<script>
  export default {
    data () {
      return {
        min: -50,
        max: 90,
        slider: 40,
      }
    },
  }
</script>

```

# Vuetify component v-slider - prop icons

Example code

```vue
<template>
  <div>
    <div class="text-caption">Media volume</div>

    <v-slider
      v-model="media"
      prepend-icon="mdi-volume-high"
    ></v-slider>

    <div class="text-caption">Alarm volume</div>

    <v-slider
      v-model="alarm"
      append-icon="mdi-alarm"
    ></v-slider>

    <div class="text-caption">Icon click callback</div>

    <v-slider
      v-model="zoom"
      append-icon="mdi-magnify-plus-outline"
      prepend-icon="mdi-magnify-minus-outline"
      @click:append="zoomIn"
      @click:prepend="zoomOut"
    ></v-slider>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const media = ref(0)
  const alarm = ref(0)
  const zoom = ref(0)

  function zoomOut () {
    zoom.value = (zoom.value - 10) || 0
  }
  function zoomIn () {
    zoom.value = (zoom.value + 10) || 100
  }
</script>

<script>
  export default {
    data () {
      return {
        media: 0,
        alarm: 0,
        zoom: 0,
      }
    },

    methods: {
      zoomOut () {
        this.zoom = (this.zoom - 10) || 0
      },
      zoomIn () {
        this.zoom = (this.zoom + 10) || 100
      },
    },
  }
</script>

```

# Vuetify component v-slider - prop readonly

Example code

```vue
<template>
  <v-slider
    label="Readonly"
    model-value="30"
    readonly
  ></v-slider>
</template>

```

# Vuetify component v-slider - prop thumb

Example code

```vue
<template>
  <div class="d-flex flex-column">
    <div>
      <div class="text-caption">
        Show thumb when using slider
      </div>
      <v-slider
        v-model="slider1"
        thumb-label
      ></v-slider>
    </div>

    <div>
      <div class="text-caption">
        Always show thumb label
      </div>
      <v-slider
        v-model="slider2"
        thumb-label="always"
      ></v-slider>
    </div>

    <div>
      <div class="text-caption">
        Custom thumb size
      </div>
      <v-slider
        v-model="slider3"
        :thumb-size="36"
        thumb-label="always"
      ></v-slider>
    </div>

    <div>
      <div class="text-caption">
        Custom thumb label
      </div>
      <v-slider
        v-model="slider4"
        thumb-label="always"
      >
        <template v-slot:thumb-label="{ modelValue }">
          {{ satisfactionEmojis[Math.min(Math.floor(modelValue / 10), 9)] }}
        </template>
      </v-slider>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const slider1 = ref(50)
  const slider2 = ref(50)
  const slider3 = ref(50)
  const slider4 = ref(50)

  const satisfactionEmojis = ['\uD83D\uDE2D', '\uD83D\uDE22', '\u2639\uFE0F', '\uD83D\uDE41', '\uD83D\uDE10', '\uD83D\uDE42', '\uD83D\uDE0A', '\uD83D\uDE01', '\uD83D\uDE04', '\uD83D\uDE0D']
</script>

<script>
  export default {
    data () {
      return {
        slider1: 50,
        slider2: 50,
        slider3: 50,
        slider4: 50,
        satisfactionEmojis: ['😭', '😢', '☹️', '🙁', '😐', '🙂', '😊', '😁', '😄', '😍'],
      }
    },
  }
</script>

```

# Vuetify component v-slider - prop disabled

Example code

```vue
<template>
  <v-slider
    model-value="30"
    disabled
  ></v-slider>
</template>

```

# Vuetify component v-slider - prop vertical

Example code

```vue
<template>
  <v-slider
    v-model="value"
    direction="vertical"
    label="Regular"
  ></v-slider>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref(10)
</script>

<script>
  export default {
    data () {
      return {
        value: 10,
      }
    },
  }
</script>

```

# Vuetify component v-slider - prop step

Example code

```vue
<template>
  <v-slider
    v-model="value"
    :max="1"
    :min="0"
    :step="0.2"
    thumb-label
  ></v-slider>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref(0)
</script>

<script>
  export default {
    data () {
      return {
        value: 0,
      }
    },
  }
</script>

```

# Vuetify component v-slider - prop colors

Example code

```vue
<template>
  <div>
    <v-slider
      v-model="slider1"
      color="orange"
      label="color"
    ></v-slider>

    <v-slider
      v-model="slider2"
      label="track-color"
      track-color="green"
    ></v-slider>

    <v-slider
      v-model="slider3"
      label="thumb-color"
      thumb-color="purple"
    ></v-slider>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const slider1 = ref(0)
  const slider2 = ref(50)
  const slider3 = ref(100)
</script>

<script>
  export default {
    data: () => ({
      slider1: 0,
      slider2: 50,
      slider3: 100,
    }),
  }
</script>

```
