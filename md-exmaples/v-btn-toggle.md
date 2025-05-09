# Vuetify component v-btn-toggle - usage

Example code

```vue
<template>
  <v-container>
    <v-row>
      <v-col
        class="py-2"
        cols="12"
        sm="6"
      >
        <p>Exclusive</p>

        <v-btn-toggle v-model="toggle_exclusive">
          <v-btn>
            <v-icon>mdi-format-align-left</v-icon>
          </v-btn>

          <v-btn>
            <v-icon>mdi-format-align-center</v-icon>
          </v-btn>

          <v-btn>
            <v-icon>mdi-format-align-right</v-icon>
          </v-btn>

          <v-btn>
            <v-icon>mdi-format-align-justify</v-icon>
          </v-btn>
        </v-btn-toggle>
      </v-col>

      <v-col
        class="py-2"
        cols="12"
        sm="6"
      >
        <p>Multiple</p>

        <v-btn-toggle
          v-model="toggle_multiple"
          color="primary"
          multiple
        >
          <v-btn>
            <v-icon>mdi-format-bold</v-icon>
          </v-btn>

          <v-btn>
            <v-icon>mdi-format-italic</v-icon>
          </v-btn>

          <v-btn>
            <v-icon>mdi-format-underline</v-icon>
          </v-btn>

          <v-btn>
            <v-icon>mdi-format-color-fill</v-icon>
          </v-btn>
        </v-btn-toggle>
      </v-col>

      <v-col
        class="py-2"
        cols="12"
        sm="6"
      >
        <p>No Options Selected</p>

        <v-btn-toggle v-model="toggle_none">
          <v-btn>
            <v-icon>mdi-format-align-left</v-icon>
          </v-btn>

          <v-btn>
            <v-icon>mdi-format-align-center</v-icon>
          </v-btn>
          <v-btn>
            <v-icon>mdi-format-align-right</v-icon>
          </v-btn>

          <v-btn>
            <v-icon>mdi-format-align-justify</v-icon>
          </v-btn>
        </v-btn-toggle>
      </v-col>

      <v-col
        class="py-2"
        cols="12"
        sm="6"
      >
        <p>Mandatory</p>

        <v-btn-toggle v-model="toggle_one" mandatory>
          <v-btn>
            <v-icon>mdi-format-align-left</v-icon>
          </v-btn>

          <v-btn>
            <v-icon>mdi-format-align-center</v-icon>
          </v-btn>

          <v-btn>
            <v-icon>mdi-format-align-right</v-icon>
          </v-btn>

          <v-btn>
            <v-icon>mdi-format-align-justify</v-icon>
          </v-btn>
        </v-btn-toggle>
      </v-col>

      <v-col
        class="py-2"
        cols="12"
      >
        <p>Text Options</p>

        <v-btn-toggle
          v-model="text"
          color="deep-purple-accent-3"
          rounded="0"
          group
        >
          <v-btn value="left">
            Left
          </v-btn>

          <v-btn value="center">
            Center
          </v-btn>

          <v-btn value="right">
            Right
          </v-btn>

          <v-btn value="justify">
            Justify
          </v-btn>
        </v-btn-toggle>
      </v-col>

      <v-col
        class="py-2"
        cols="12"
      >
        <p>Text &amp; Icon Options</p>

        <v-btn-toggle v-model="icon" divided>
          <v-btn value="left">
            <span class="hidden-sm-and-down">Left</span>

            <v-icon end>
              mdi-format-align-left
            </v-icon>
          </v-btn>

          <v-btn value="center">
            <span class="hidden-sm-and-down">Center</span>

            <v-icon end>
              mdi-format-align-center
            </v-icon>
          </v-btn>

          <v-btn value="right">
            <span class="hidden-sm-and-down">Right</span>

            <v-icon end>
              mdi-format-align-right
            </v-icon>
          </v-btn>

          <v-btn value="justify">
            <span class="hidden-sm-and-down">Justify</span>

            <v-icon end>
              mdi-format-align-justify
            </v-icon>
          </v-btn>
        </v-btn-toggle>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        text: 'center',
        icon: 'justify',
        toggle_none: null,
        toggle_one: 0,
        toggle_exclusive: 2,
        toggle_multiple: [0, 1, 2],
      }
    },
  }
</script>

```

# Vuetify component v-btn-toggle - prop variant

Example code

```vue
<template>
  <div class="d-flex align-center flex-column bg-grey-lighten-4 pa-6">
    <div class="text-subtitle-2">Default</div>
    <v-btn-toggle
      v-model="toggle"
      color="primary"
    >
      <v-btn icon="mdi-format-align-left"></v-btn>
      <v-btn icon="mdi-format-align-center"></v-btn>
      <v-btn icon="mdi-format-align-right"></v-btn>
      <v-btn icon="mdi-format-align-justify"></v-btn>
    </v-btn-toggle>

    <div class="mt-6 text-subtitle-2">Text</div>
    <v-btn-toggle
      v-model="toggle"
      color="primary"
      variant="text"
    >
      <v-btn icon="mdi-format-align-left"></v-btn>
      <v-btn icon="mdi-format-align-center"></v-btn>
      <v-btn icon="mdi-format-align-right"></v-btn>
      <v-btn icon="mdi-format-align-justify"></v-btn>
    </v-btn-toggle>

    <div class="mt-6 text-subtitle-2">Plain</div>
    <v-btn-toggle
      v-model="toggle"
      color="primary"
      variant="plain"
    >
      <v-btn icon="mdi-format-align-left"></v-btn>
      <v-btn icon="mdi-format-align-center"></v-btn>
      <v-btn icon="mdi-format-align-right"></v-btn>
      <v-btn icon="mdi-format-align-justify"></v-btn>
    </v-btn-toggle>

    <div class="mt-6 text-subtitle-2">Outlined</div>
    <v-btn-toggle
      v-model="toggle"
      color="primary"
      variant="outlined"
    >
      <v-btn icon="mdi-format-align-left"></v-btn>
      <v-btn icon="mdi-format-align-center"></v-btn>
      <v-btn icon="mdi-format-align-right"></v-btn>
      <v-btn icon="mdi-format-align-justify"></v-btn>
    </v-btn-toggle>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const toggle = ref(null)
</script>

<script>
  export default {
    data: () => ({
      toggle: null,
    }),
  }
</script>

```

# Vuetify component v-btn-toggle - prop rounded

Example code

```vue
<template>
  <div class="d-flex justify-space-around bg-grey-lighten-4 pa-6">
    <v-btn-toggle
      rounded="0"
    >
      <v-btn icon="mdi-format-align-left"></v-btn>
      <v-btn icon="mdi-format-align-center"></v-btn>
      <v-btn icon="mdi-format-align-right"></v-btn>
      <v-btn icon="mdi-format-align-justify"></v-btn>
    </v-btn-toggle>

    <v-btn-toggle
      rounded="xl"
    >
      <v-btn icon="mdi-format-align-left"></v-btn>
      <v-btn icon="mdi-format-align-center"></v-btn>
      <v-btn icon="mdi-format-align-right"></v-btn>
      <v-btn icon="mdi-format-align-justify"></v-btn>
    </v-btn-toggle>
  </div>
</template>

```

# Vuetify component v-btn-toggle - prop multiple

Example code

```vue
<template>
  <div class="d-flex flex-column align-center bg-grey-lighten-4 pa-6">
    <v-btn-toggle
      v-model="toggle"
      multiple
    >
      <v-btn icon="mdi-format-align-left" value="left"></v-btn>
      <v-btn icon="mdi-format-align-center" value="center"></v-btn>
      <v-btn icon="mdi-format-align-right" value="right"></v-btn>
      <v-btn icon="mdi-format-align-justify" value="justify"></v-btn>
    </v-btn-toggle>

    <pre class="pt-2">{{ toggle }}</pre>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const toggle = ref([])
</script>

<script>
  export default {
    data () {
      return {
        toggle: [],
      }
    },
  }
</script>

```

# Vuetify component v-btn-toggle - misc wysiwyg

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="600"
  >
    <div class="d-flex justify-space-between pa-4 pb-0">
      <v-btn-toggle
        v-model="formatting"
        variant="outlined"
        divided
        multiple
      >
        <v-btn>
          <v-icon icon="mdi-format-italic"></v-icon>
        </v-btn>

        <v-btn>
          <v-icon icon="mdi-format-bold"></v-icon>
        </v-btn>

        <v-btn>
          <v-icon icon="mdi-format-underline"></v-icon>
        </v-btn>

        <v-btn>
          <div class="d-flex align-center flex-column justify-center">
            <v-icon icon="mdi-format-color-text"></v-icon>

            <v-sheet
              color="purple"
              height="4"
              width="26"
              tile
            ></v-sheet>
          </div>
        </v-btn>
      </v-btn-toggle>

      <v-btn-toggle
        v-model="alignment"
        variant="outlined"
        divided
      >
        <v-btn>
          <v-icon icon="mdi-format-align-center"></v-icon>
        </v-btn>

        <v-btn>
          <v-icon icon="mdi-format-align-left"></v-icon>
        </v-btn>

        <v-btn>
          <v-icon icon="mdi-format-align-right"></v-icon>
        </v-btn>
      </v-btn-toggle>
    </div>

    <v-sheet class="pa-4 text-center">
      <v-textarea
        v-model="value"
        rows="2"
        variant="outlined"
        auto-grow
        hide-details
      ></v-textarea>
    </v-sheet>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const alignment = ref(1)
  const formatting = ref([])
  const value = ref('Toggle button requirements.\n\nHave at least three toggle buttons in a group\nLabel buttons with text, an icon, or')
</script>

<script>
  export default {
    data: () => ({
      alignment: 1,
      formatting: [],
      value: 'Toggle button requirements.\n\nHave at least three toggle buttons in a group\nLabel buttons with text, an icon, or',
    }),
  }
</script>

```

# Vuetify component v-btn-toggle - prop mandatory

Example code

```vue
<template>
  <div class="d-flex flex-column align-center bg-grey-lighten-4 pa-6">
    <v-btn-toggle
      v-model="toggle"
      color="primary"
      mandatory
    >
      <v-btn icon="mdi-format-align-left" value="left"></v-btn>
      <v-btn icon="mdi-format-align-center" value="center"></v-btn>
      <v-btn icon="mdi-format-align-right" value="right"></v-btn>
      <v-btn icon="mdi-format-align-justify" value="justify"></v-btn>
    </v-btn-toggle>
    <pre class="pt-2">{{ toggle }}</pre>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const toggle = ref()
</script>

<script>
  export default {
    data () {
      return {
        toggle: undefined,
      }
    },
  }
</script>

```

# Vuetify component v-btn-toggle - misc toolbar

Example code

```vue
<template>
  <v-toolbar>
    <!-- <v-overflow-btn
      :items="dropdown_font"
      label="Select font"
      hide-details
      class="pa-0"
    ></v-overflow-btn>

    <v-divider vertical></v-divider>

    <v-overflow-btn
      :items="dropdown_edit"
      editable
      label="Select size"
      hide-details
      class="pa-0"
      overflow
    ></v-overflow-btn>

    <v-divider vertical></v-divider> -->

    <v-spacer></v-spacer>

    <v-btn-toggle
      v-model="toggleMultiple"
      color="primary"
      variant="plain"
      multiple
    >
      <v-btn
        :value="1"
        icon="mdi-format-bold"
      ></v-btn>

      <v-btn
        :value="2"
        icon="mdi-format-italic"
      ></v-btn>

      <v-btn
        :value="3"
        icon="mdi-format-underline"
      ></v-btn>

      <v-btn
        :value="4"
        icon="mdi-format-color-fill"
      ></v-btn>
    </v-btn-toggle>

    <div class="mx-4"></div>

    <v-btn-toggle
      v-model="toggleExclusive"
      color="primary"
      density="compact"
      variant="plain"
    >
      <v-btn
        :value="1"
        icon="mdi-format-align-left"
      ></v-btn>

      <v-btn
        :value="2"
        icon="mdi-format-align-center"
      ></v-btn>

      <v-btn
        :value="3"
        icon="mdi-format-align-right"
      ></v-btn>

      <v-btn
        :value="4"
        icon="mdi-format-align-justify"
      ></v-btn>
    </v-btn-toggle>
  </v-toolbar>
</template>

<script setup>
  import { ref } from 'vue'

  const toggleExclusive = ref(2)
  const toggleMultiple = ref([1, 2, 3])
</script>

<script>
  export default {
    data () {
      return {
        toggleExclusive: 2,
        toggleMultiple: [1, 2, 3],
      }
    },
  }
</script>

```

# Vuetify component v-btn-toggle - prop divided

Example code

```vue
<template>
  <div class="d-flex align-center flex-column bg-grey-lighten-4 pa-6">
    <v-btn-toggle
      v-model="toggle"
      divided
    >
      <v-btn icon="mdi-format-align-left"></v-btn>
      <v-btn icon="mdi-format-align-center"></v-btn>
      <v-btn icon="mdi-format-align-right"></v-btn>
      <v-btn icon="mdi-format-align-justify"></v-btn>
    </v-btn-toggle>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const toggle = ref(null)
</script>

<script>
  export default {
    data: () => ({
      toggle: null,
    }),
  }
</script>

```
