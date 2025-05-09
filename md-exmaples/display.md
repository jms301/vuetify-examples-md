# Vuetify concept display - display block

Example code

```vue
<template>
  <div>
    <div class="d-block pa-2 bg-deep-purple">
      d-block
    </div>
    <div class="d-block pa-2 bg-black">
      d-block
    </div>
  </div>
</template>

```

# Vuetify concept display - hidden elements

Example code

```vue
<template>
  <v-toolbar light>
    <v-toolbar-title>Title</v-toolbar-title>
    <v-toolbar-items
      v-for="item in items"
      :key="item.text"
      class="hidden-sm-and-down"
    >
      <v-btn variant="text">
        {{ item.text }}
      </v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script setup>
  const items = [
    {
      text: 'Link One',
    },
    {
      text: 'Link Two',
    },
    {
      text: 'Link Three',
    },
  ]
</script>

<script>
  export default {
    data () {
      return {
        items: [
          {
            text: 'Link One',
          },
          {
            text: 'Link Two',
          },
          {
            text: 'Link Three',
          },
        ],
      }
    },
  }
</script>

```

# Vuetify concept display - visibility

Example code

```vue
<template>
  <div>
    <div class="d-lg-none">
      hide on screens wider than lg
    </div>
    <div class="d-none d-lg-block">
      hide on screens smaller than lg
    </div>
  </div>
</template>

```

# Vuetify concept display - display inline

Example code

```vue
<template>
  <div>
    <div class="d-inline pa-2 bg-deep-purple">
      d-inline
    </div>
    <div class="d-inline pa-2 bg-black">
      d-inline
    </div>
  </div>
</template>

```

# Vuetify concept display - print

Example code

```vue
<template>
  <div>
    <div class="d-print-none">
      Screen Only (Hide on print only)
    </div>
    <div class="d-none d-print-block">
      Print Only (Hide on screen only)
    </div>
    <div class="d-none d-lg-block d-print-block">
      Hide up to large on screen, but always show on print
    </div>
  </div>
</template>

```
