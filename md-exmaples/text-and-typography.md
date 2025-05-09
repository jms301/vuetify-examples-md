# Vuetify concept text-and-typography - typography breakpoints

Example code

```vue
<template>
  <div class="d-flex justify-center">
    <v-card width="300px">
      <v-card-title class="text-h6 text-md-h5 text-lg-h4">Title</v-card-title>
      <v-card-text>
        Body text
      </v-card-text>
    </v-card>
  </div>
</template>

```

# Vuetify concept text-and-typography - text decoration

Example code

```vue
<template>
  <div class="d-flex justify-space-between flex-row">
    <a
      class="text-decoration-none"
      href="#"
    >
      Non-underlined link
    </a>

    <div class="text-decoration-line-through">
      Line-through text
    </div>

    <div class="text-decoration-overline">
      Overline text
    </div>

    <div class="text-decoration-underline">
      Underline text
    </div>
  </div>
</template>

```

# Vuetify concept text-and-typography - typography

Example code

```vue
<template>
  <div>
    <v-card v-for="[name, cls] in classes" :key="name" class="my-4">
      <div :class="[cls, 'pa-2']">{{ name }}</div>
      <div class="text-caption pa-2 bg-grey-lighten-4">
        <div class="text-grey">Class</div>
        <div class="font-weight-medium">{{ cls }}</div>
      </div>
    </v-card>
  </div>
</template>

<script setup>
  const classes = [
    ['Heading 1', 'text-h1'],
    ['Heading 2', 'text-h2'],
    ['Heading 3', 'text-h3'],
    ['Heading 4', 'text-h4'],
    ['Heading 5', 'text-h5'],
    ['Heading 6', 'text-h6'],
    ['Subtitle 1', 'text-subtitle-1'],
    ['Subtitle 2', 'text-subtitle-2'],
    ['Body 1', 'text-body-1'],
    ['Body 2', 'text-body-2'],
    ['Button', 'text-button'],
    ['Caption', 'text-caption'],
    ['Overline', 'text-overline'],
  ]
</script>

<script>
  export default {
    data: () => ({
      classes: [
        ['Heading 1', 'text-h1'],
        ['Heading 2', 'text-h2'],
        ['Heading 3', 'text-h3'],
        ['Heading 4', 'text-h4'],
        ['Heading 5', 'text-h5'],
        ['Heading 6', 'text-h6'],
        ['Subtitle 1', 'text-subtitle-1'],
        ['Subtitle 2', 'text-subtitle-2'],
        ['Body 1', 'text-body-1'],
        ['Body 2', 'text-body-2'],
        ['Button', 'text-button'],
        ['Caption', 'text-caption'],
        ['Overline', 'text-overline'],
      ],
    }),
  }
</script>

```

# Vuetify concept text-and-typography - text transform

Example code

```vue
<template>
  <div>
    <p class="text-lowercase">
      Lowercased text.
    </p>
    <p class="text-uppercase">
      Uppercased text.
    </p>
    <p class="text-capitalize">
      capitalized text.
    </p>
  </div>
</template>

```

# Vuetify concept text-and-typography - text rtl

Example code

```vue
<template>
  <div>
    <p class="text-subtitle-2 text-center">
      Agnostic RTL Alignment
    </p>

    <p class="text-left">
      Left aligned text, irrespective of RTL or LTR.
    </p>
    <p class="text-right">
      Right aligned text, irrespective of RTL or LTR.
    </p>

    <p class="text-subtitle-2 text-center">
      Responsive RTL Alignment
    </p>

    <p class="text-start">
      Left aligned text on LTR and right aligned on RTL.
    </p>
    <p class="text-end">
      Right aligned text on LTR and left aligned on RTL.
    </p>
  </div>
</template>

```

# Vuetify concept text-and-typography - text alignment

Example code

```vue
<template>
  <div>
    <p class="text-left">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    </p>

    <p class="text-right">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    </p>

    <p class="text-center">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    </p>

    <p class="text-justify">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    </p>

    <p class="text-start">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    </p>

    <p class="text-end">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    </p>
  </div>
</template>

```

# Vuetify concept text-and-typography - text break

Example code

```vue
<template>
  <div>
    <p class="custom-transform-class text-none">
      Random TEXT cApitaLization
    </p>
    <p
      class="text-break"
      style="max-width: 4rem;"
    >
      SUBDERMATOGLYPHIC
    </p>
  </div>
</template>

<style lang="sass">
  .custom-transform-class
    text-transform: uppercase
</style>

```

# Vuetify concept text-and-typography - text truncate

Example code

```vue
<template>
  <div>
    <span
      class="d-inline-block text-truncate"
      style="max-width: 150px;"
    >
      Suspendisse faucibus, nunc et pellentesque egestas, lacus ante convallis tellus.
    </span>
  </div>
</template>

```

# Vuetify concept text-and-typography - font emphasis

Example code

```vue
<template>
  <div>
    <p class="font-weight-black">
      Black text.
    </p>
    <p class="font-weight-bold">
      Bold text.
    </p>
    <p class="font-weight-medium">
      Medium weight text.
    </p>
    <p class="font-weight-regular">
      Normal weight text.
    </p>
    <p class="font-weight-light">
      Light weight text.
    </p>
    <p class="font-weight-thin">
      Thin weight text.
    </p>
    <p class="font-italic">
      Italic text.
    </p>
  </div>
</template>

```

# Vuetify concept text-and-typography - text no wrap

Example code

```vue
<template>
  <div
    class="text-no-wrap bg-secondary"
    style="width: 8rem;"
  >
    This text should overflow the parent.
  </div>
</template>

```

# Vuetify concept text-and-typography - text opacity

Example code

```vue
<template>
  <div>
    <p class="text-high-emphasis">
      High-emphasis has an opacity of 87% in light theme and 100% in dark.
    </p>
    <p class="text-medium-emphasis">
      Medium-emphasis text and hint text have opacities of 60% in light theme and 70% in dark.
    </p>
    <p class="text-disabled">
      Disabled text has an opacity of 38% in light theme and 50% in dark.
    </p>
  </div>
</template>

```

# Vuetify concept text-and-typography - text alignment responsive

Example code

```vue
<template>
  <div>
    <p class="text-left">
      Left aligned on all viewport sizes.
    </p>
    <p class="text-center">
      Center aligned on all viewport sizes.
    </p>
    <p class="text-right">
      Right aligned on all viewport sizes.
    </p>

    <p class="text-sm-left">
      Left aligned on viewports SM (small) or wider.
    </p>
    <p class="text-right text-md-left">
      Left aligned on viewports MD (medium) or wider.
    </p>
    <p class="text-right text-lg-left">
      Left aligned on viewports LG (large) or wider.
    </p>
    <p class="text-right text-xl-left">
      Left aligned on viewports XL (extra-large) or wider.
    </p>
  </div>
</template>

```
