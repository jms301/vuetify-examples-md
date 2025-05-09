# Vuetify concept grid - usage

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row no-gutters>
      <v-col
        v-for="n in 3"
        :key="n"
        cols="12"
        sm="4"
      >
        <v-sheet class="ma-2 pa-2">
          One of three columns
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - misc grow and shrink

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row
      class="mb-6"
      no-gutters
    >
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
    </v-row>

    <v-row no-gutters>
      <v-col cols="8">
        <v-sheet class="pa-2 ma-2">
          .v-col-8
        </v-sheet>
      </v-col>

      <v-col cols="4">
        <v-sheet class="pa-2 ma-2">
          .v-col-4
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - prop breakpoint sizing

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row no-gutters>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
    </v-row>

    <v-row no-gutters>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
    </v-row>

    <v-row no-gutters>
      <v-col cols="2">
        <v-sheet class="pa-2 ma-2">
          .v-col-2
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - misc margin helpers

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row>
      <v-col md="4">
        <v-sheet class="pa-2 ma-2">
          .v-col-md-4
        </v-sheet>
      </v-col>
      <v-col
        class="ms-auto"
        md="4"
      >
        <v-sheet class="pa-2 ma-2">
          .v-col-md-4 .ms-auto
        </v-sheet>
      </v-col>
    </v-row>

    <v-row>
      <v-col
        class="ms-md-auto"
        md="4"
      >
        <v-sheet class="pa-2 ma-2">
          .v-col-md-4 .ms-md-auto
        </v-sheet>
      </v-col>
      <v-col
        class="ms-md-auto"
        md="4"
      >
        <v-sheet class="pa-2 ma-2">
          .v-col-md-4 .ms-md-auto
        </v-sheet>
      </v-col>
    </v-row>

    <v-row>
      <v-col
        class="me-auto"
        cols="auto"
      >
        <v-sheet class="pa-2 ma-2">
          .v-col-auto .me-auto
        </v-sheet>
      </v-col>
      <v-col cols="auto">
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - misc variable content

Example code

```vue
<template>
  <v-container class="bg-grey-lighten-5">
    <v-row
      class="mb-6"
      justify="center"
      no-gutters
    >
      <v-col lg="2">
        <v-card
          class="pa-2"
          rounded="0"
          variant="outlined"
        >
          1 of 3
        </v-card>
      </v-col>
      <v-col md="auto">
        <v-card
          class="pa-2"
          rounded="0"
          variant="outlined"
        >
          Variable width content
        </v-card>
      </v-col>
      <v-col lg="2">
        <v-card
          class="pa-2"
          rounded="0"
          variant="outlined"
        >
          3 of 3
        </v-card>
      </v-col>
    </v-row>
    <v-row no-gutters>
      <v-col>
        <v-card
          class="pa-2"
          rounded="0"
          variant="outlined"
        >
          1 of 3
        </v-card>
      </v-col>
      <v-col md="auto">
        <v-card
          class="pa-2"
          rounded="0"
          variant="outlined"
        >
          Variable width content
        </v-card>
      </v-col>
      <v-col lg="2">
        <v-card
          class="pa-2"
          rounded="0"
          variant="outlined"
        >
          3 of 3
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - prop offset

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row
      class="mb-6"
      no-gutters
    >
      <v-col cols="4">
        <v-sheet class="pa-2 ma-2">
          .v-col-4
        </v-sheet>
      </v-col>
      <v-col
        cols="4"
        offset="4"
      >
        <v-sheet class="pa-2 ma-2">
          .v-col-4 .offset-4
        </v-sheet>
      </v-col>
    </v-row>
    <v-row
      class="mb-6"
      no-gutters
    >
      <v-col
        cols="3"
        offset="3"
      >
        <v-sheet class="pa-2 ma-2">
          .v-col-3 .offset-3
        </v-sheet>
      </v-col>
      <v-col
        cols="3"
        offset="3"
      >
        <v-sheet class="pa-2 ma-2">
          .v-col-3 .offset-3
        </v-sheet>
      </v-col>
    </v-row>
    <v-row no-gutters>
      <v-col
        cols="6"
        offset="3"
      >
        <v-sheet class="pa-2 ma-2">
          .v-col-6 .offset-3
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - prop order

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row no-gutters>
      <v-col order="6">
        <v-sheet class="pa-2 ma-2">
          First in markup, but middle in row
        </v-sheet>
      </v-col>
      <v-col order="12">
        <v-sheet class="pa-2 ma-2">
          Second in markup, but last in row
        </v-sheet>
      </v-col>
      <v-col order="1">
        <v-sheet class="pa-2 ma-2">
          Third in markup, but first in row
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - misc one column width

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row no-gutters>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-col cols="6">
        <v-sheet class="pa-2 ma-2">
          .v-col-6
        </v-sheet>
      </v-col>

      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
    </v-row>

    <v-row no-gutters>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-col cols="2">
        <v-sheet class="pa-2 ma-2">
          .v-col-2
        </v-sheet>
      </v-col>

      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - misc equal width columns

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row no-gutters>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-responsive width="100%"></v-responsive>

      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - misc spacer

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-spacer></v-spacer>

      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-spacer></v-spacer>

      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>

      <v-spacer></v-spacer>

      <v-col>
        <v-sheet class="pa-2 ma-2">
          .v-col-auto
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - misc unique layouts

Example code

```vue
<template>
  <v-container class="bg-grey-lighten-5">
    <!-- Stack the columns on mobile by making one full-width and the other half-width -->
    <v-row>
      <v-col
        cols="12"
        md="8"
      >
        <v-card
          class="pa-2"
          rounded="0"
          variant="outlined"
        >
          .col-12 .col-md-8
        </v-card>
      </v-col>
      <v-col
        cols="6"
        md="4"
      >
        <v-card
          class="pa-2"
          rounded="0"
          variant="outlined"
        >
          .col-6 .col-md-4
        </v-card>
      </v-col>
    </v-row>

    <!-- Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop -->
    <v-row>
      <v-col
        v-for="n in 3"
        :key="n"
        cols="6"
        md="4"
      >
        <v-card
          class="pa-2"
          rounded="0"
          variant="outlined"
        >
          .col-6 .col-md-4
        </v-card>
      </v-col>
    </v-row>

    <!-- Columns are always 50% wide, on mobile and desktop -->
    <v-row>
      <v-col
        v-for="n in 2"
        :key="n"
        cols="6"
      >
        <v-card
          class="pa-2"
          rounded="0"
          variant="outlined"
        >
          .col-6
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - prop no gutters

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row no-gutters>
      <v-col cols="12">
        <v-sheet class="pa-2">
          .v-col-12
        </v-sheet>
      </v-col>
      <v-col cols="6">
        <v-sheet class="pa-2">
          .v-col-6
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - prop justify

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row justify="start">
      <v-col
        v-for="k in 2"
        :key="k"
        cols="4"
      >
        <v-sheet class="pa-2 ma-2">
          .justify-start
        </v-sheet>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col
        v-for="k in 2"
        :key="k"
        cols="4"
      >
        <v-sheet class="pa-2 ma-2">
          .justify-center
        </v-sheet>
      </v-col>
    </v-row>

    <v-row justify="end">
      <v-col
        v-for="k in 2"
        :key="k"
        cols="4"
      >
        <v-sheet class="pa-2 ma-2">
          .justify-end
        </v-sheet>
      </v-col>
    </v-row>

    <v-row justify="space-around">
      <v-col
        v-for="k in 2"
        :key="k"
        cols="4"
      >
        <v-sheet class="pa-2 ma-2">
          .justify-space-around
        </v-sheet>
      </v-col>
    </v-row>

    <v-row justify="space-between">
      <v-col
        v-for="k in 2"
        :key="k"
        cols="4"
      >
        <v-sheet class="pa-2 ma-2">
          .justify-space-between
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - misc column wrapping

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row no-gutters>
      <v-col cols="9">
        <v-sheet class="pa-2 ma-2">
          .v-col-9
        </v-sheet>
      </v-col>
      <v-col cols="4">
        <v-sheet class="pa-2 ma-2">
          .v-col-4
        </v-sheet>
      </v-col>
      <v-col cols="6">
        <v-sheet class="pa-2 ma-2">
          .v-col-6
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - misc nested grid

Example code

```vue
<template>
  <v-container>
    <v-row class="bg-green">
      <v-col cols="8">
        <v-sheet class="pa-2 ma-2">
          Level 1: .v-col-8
        </v-sheet>

        <v-row class="bg-red" no-gutters>
          <v-col
            cols="8"
          >
            <v-sheet class="pa-2 ma-2">
              Level 2: .v-col-8
            </v-sheet>
          </v-col>

          <v-col
            cols="4"
          >
            <v-sheet class="pa-2 ma-2">
              Level 2: .v-col-4
            </v-sheet>
          </v-col>
        </v-row>
      </v-col>

      <v-col cols="4">
        <v-sheet class="pa-2 ma-2">
          Level 1: .v-col-4
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - prop order first and last

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row no-gutters>
      <v-col order="last">
        <v-sheet class="pa-2 ma-2">
          First, but last
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="pa-2 ma-2">
          Second, but unordered
        </v-sheet>
      </v-col>
      <v-col order="first">
        <v-sheet class="pa-2 ma-2">
          Third, but first
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept grid - misc row and column breakpoints

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row
      class="mb-6"
      no-gutters
    >
      <v-col :cols="cols[0]">
        <v-sheet class="pa-2 ma-2">
          .v-col-{{ cols[0] }}
        </v-sheet>
      </v-col>

      <v-col :cols="cols[1]">
        <v-sheet class="pa-2 ma-2">
          .v-col-{{ cols[1] }}
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { computed } from 'vue'
  import { useDisplay } from 'vuetify'

  const { lg, sm } = useDisplay()

  const cols = computed(() => {
    return lg.value ? [3, 9]
      : sm.value ? [9, 3]
        : [6, 6]
  })
</script>

<script>
  export default {
    computed: {
      cols () {
        const { lg, sm } = this.$vuetify.display
        return lg ? [3, 9]
          : sm ? [9, 3]
            : [6, 6]
      },
    },
  }
</script>

```

# Vuetify concept grid - prop align

Example code

```vue
<template>
  <div>
    <v-container
      class="bg-surface-variant mb-6"
    >
      <v-row
        align="start"
        style="height: 150px;"
        no-gutters
      >
        <v-col
          v-for="n in 3"
          :key="n"
        >
          <v-sheet class="pa-2 ma-2">
            .align-start
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>

    <v-container
      class="bg-surface-variant mb-6"
    >
      <v-row
        align="center"
        style="height: 150px;"
        no-gutters
      >
        <v-col
          v-for="n in 3"
          :key="n"
        >
          <v-sheet class="pa-2 ma-2">
            .align-center
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>

    <v-container
      class="bg-surface-variant mb-6"
    >
      <v-row
        align="end"
        style="height: 150px;"
        no-gutters
      >
        <v-col
          v-for="n in 3"
          :key="n"
        >
          <v-sheet class="pa-2 ma-2">
            .align-end
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>

    <v-container class="bg-surface-variant">
      <v-row
        style="height: 150px;"
        no-gutters
      >
        <v-col align-self="start">
          <v-sheet class="pa-2 ma-2">
            .align-self-start
          </v-sheet>
        </v-col>

        <v-col align-self="center">
          <v-sheet class="pa-2 ma-2">
            .align-self-center
          </v-sheet>
        </v-col>

        <v-col align-self="end">
          <v-sheet class="pa-2 ma-2">
            .align-self-end
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

```

# Vuetify concept grid - prop offset breakpoint

Example code

```vue
<template>
  <v-container class="bg-surface-variant">
    <v-row
      class="mb-6"
      no-gutters
    >
      <v-col
        md="6"
        sm="5"
      >
        <v-sheet class="pa-2 ma-2">
          .v-col-sm-5 .v-col-md-6
        </v-sheet>
      </v-col>
      <v-col
        md="6"
        offset-md="0"
        offset-sm="2"
        sm="5"
      >
        <v-sheet class="pa-2 ma-2">
          .v-col-sm-5 .offset-sm-2 .v-col-md-6 .offset-md-0
        </v-sheet>
      </v-col>
    </v-row>
    <v-row no-gutters>
      <v-col
        lg="6"
        md="5"
        sm="6"
      >
        <v-sheet class="pa-2 ma-2">
          sm-6 md-5 lg-6
        </v-sheet>
      </v-col>
      <v-col
        lg="6"
        md="5"
        offset-lg="0"
        offset-md="2"
        sm="6"
      >
        <v-sheet class="pa-2 ma-2">
          .v-col-sm-6 md-5 .offset-md-2 .v-col-lg-6 .offset-lg-0
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```
