# Vuetify component v-scroll - usage

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <h3
          ref="radio"
          class="text-h5"
        >
          Target
        </h3>

        <v-radio-group
          v-model="type"
          inline
        >
          <v-radio
            label="Number"
            value="number"
          ></v-radio>

          <v-radio
            label="Selector"
            value="selector"
          ></v-radio>

          <v-radio
            label="DOMElement"
            value="element"
          ></v-radio>
        </v-radio-group>

        <v-text-field
          v-if="type === 'number'"
          v-model="number"
          label="Number"
          type="number"
        ></v-text-field>

        <v-text-field
          v-if="type === 'selector'"
          v-model="selector"
          label="Selector"
        ></v-text-field>

        <v-select
          v-if="type === 'element'"
          v-model="selected"
          :items="elements"
          label="DOMElement"
        ></v-select>
      </v-col>

      <v-col cols="12">
        <h3 class="text-h5">
          Options
        </h3>

        <v-select
          v-model="easing"
          :items="easings"
          label="Easing"
        ></v-select>

        <v-slider
          v-model="duration"
          label="Duration"
          max="1000"
          min="0"
          thumb-label
        ></v-slider>

        <v-slider
          v-model="offset"
          label="Offset"
          max="500"
          min="-500"
          thumb-label
        ></v-slider>
      </v-col>

      <v-col>
        <v-btn
          ref="button"
          color="primary"
          block
          @click="$vuetify.goTo(target, options)"
        >
          scroll
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  // import * as easings from 'vuetify/lib/services/goto/easing-patterns'

  export default {
    data () {
      return {
        type: 'number',
        number: 9999,
        selector: '#scroll-with-options',
        selected: 'Button',
        elements: ['Button', 'Radio group'],
        duration: 300,
        offset: 0,
        easing: 'easeInOutCubic',
        easings: [], // TODO: fix import? Object.keys(easings),
      }
    },
    computed: {
      target () {
        const value = this[this.type]
        if (!isNaN(value)) return Number(value)
        else return value
      },
      options () {
        return {
          duration: this.duration,
          offset: this.offset,
          easing: this.easing,
        }
      },
      element () {
        if (this.selected === 'Button') return this.$refs.button
        else if (this.selected === 'Radio group') return this.$refs.radio
        else return null
      },
    },
  }
</script>

```

# Vuetify component v-scroll - option self

Example code

```vue
<template>
  <v-card
    class="overflow-y-auto"
    max-height="400"
    v-scroll.self="onScroll"
  >
    <v-banner
      class="justify-center text-h5 font-weight-light"
      sticky
    >
      Scroll Me - Method invoked

      <span
        class="font-weight-bold"
        v-text="scrollInvoked"
      ></span>

      times
    </v-banner>

    <v-card-text>
      <div
        v-for="n in 12"
        :key="n"
        class="mb-4"
      >
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi commodi earum tenetur. Asperiores dolorem placeat ab nobis iusto culpa, autem molestias molestiae quidem pariatur. Debitis beatae expedita nam facere perspiciatis. Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus ducimus cupiditate rerum officiis consequuntur laborum doloremque quaerat ipsa voluptates, nobis nam quis nulla ullam at corporis, similique ratione quasi illo!
      </div>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const scrollInvoked = ref(0)
  function onScroll () {
    scrollInvoked.value++
  }
</script>

<script>
  export default {
    data: () => ({
      scrollInvoked: 0,
    }),

    methods: {
      onScroll () {
        this.scrollInvoked++
      },
    },
  }
</script>

```

# Vuetify component v-scroll - option target

Example code

```vue
<template>
  <div>
    <v-row
      align="center"
      justify="center"
    >
      <v-col class="text-center">
        <div class="text-subtitle-2">Offset Top</div>
        {{ offsetTop }}
      </v-col>
    </v-row>
    <v-container
      id="scroll-target"
      class="overflow-y-auto"
      style="max-height: 400px"
    >
      <v-row
        align="center"
        justify="center"
        style="height: 1000px"
        v-scroll:#scroll-target="onScroll"
      >
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const offsetTop = ref(0)
  function onScroll (e) {
    offsetTop.value = e.target.scrollTop
  }
</script>

<script>
  export default {
    data: () => ({
      offsetTop: 0,
    }),

    methods: {
      onScroll (e) {
        this.offsetTop = e.target.scrollTop
      },
    },
  }
</script>

```
