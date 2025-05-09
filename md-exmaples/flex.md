# Vuetify concept flex - flex align content center

Example code

```vue
<template>
  <v-sheet
    class="d-flex align-content-center flex-wrap bg-surface-variant"
    min-height="200"
  >
    <v-sheet
      v-for="n in 20"
      :key="n"
      class="ma-2 pa-2"
    >
      Flex item
    </v-sheet>
  </v-sheet>
</template>

```

# Vuetify concept flex - margins

Example code

```vue
<template>
  <div>
    <v-sheet class="d-flex mb-6 bg-surface-variant">
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
    </v-sheet>

    <v-sheet class="d-flex mb-6 bg-surface-variant">
      <v-sheet class="ma-2 pa-2 me-auto">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
    </v-sheet>

    <v-sheet class="d-flex mb-6 bg-surface-variant">
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
    </v-sheet>
  </div>
</template>

```

# Vuetify concept flex - grow shrink

Example code

```vue
<template>
  <v-container>
    <v-row
      class="flex-nowrap bg-surface-variant"
      no-gutters
    >
      <v-col
        class="flex-grow-0 flex-shrink-0"
        cols="2"
      >
        <v-sheet class="ma-2 pa-2">
          I'm 2 column wide
        </v-sheet>
      </v-col>

      <v-col
        class="flex-grow-1 flex-shrink-0"
        cols="1"
        style="min-width: 100px; max-width: 100%;"
      >
        <v-sheet class="ma-2 pa-2">
          I'm 1 column wide and I grow to take all the space
        </v-sheet>
      </v-col>

      <v-col
        class="flex-grow-0 flex-shrink-1"
        cols="5"
        style="min-width: 100px;"
      >
        <v-sheet class="ma-2 pa-2">
          I'm 5 column wide and I shrink if there's not enough space
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept flex - flex nowrap

Example code

```vue
<template>
  <v-sheet
    class="d-flex flex-nowrap py-3 bg-surface-variant"
    width="125"
  >
    <v-sheet
      v-for="n in 5"
      :key="n"
      class="ma-2 pa-2"
    >
      Flex item
    </v-sheet>
  </v-sheet>
</template>

```

# Vuetify concept flex - flex align self

Example code

```vue
<template>
  <div>
    <v-sheet
      class="d-flex mb-6 bg-surface-variant"
      height="100"
    >
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2 align-self-start">align-self-start</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
    </v-sheet>

    <v-sheet
      class="d-flex mb-6 bg-surface-variant"
      height="100"
    >
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2 align-self-end">align-self-end</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
    </v-sheet>

    <v-sheet
      class="d-flex mb-6 bg-surface-variant"
      height="100"
    >
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2 align-self-center">align-self-center</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
    </v-sheet>

    <v-sheet
      class="d-flex mb-6 bg-surface-variant"
      height="100"
    >
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2 align-self-baseline">align-self-baseline</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
    </v-sheet>

    <v-sheet
      class="d-flex mb-6 bg-surface-variant"
      height="100"
    >
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2 align-self-auto">align-self-auto</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
    </v-sheet>

    <v-sheet
      class="d-flex mb-6 bg-surface-variant"
      height="100"
    >
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2 align-self-stretch">align-self-stretch</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
    </v-sheet>
  </div>
</template>

```

# Vuetify concept flex - flex column

Example code

```vue
<template>
  <div>
    <div class="d-flex flex-column mb-6 bg-surface-variant">
      <v-sheet class="ma-2 pa-2">Flex item 1</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item 2</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item 3</v-sheet>
    </div>

    <div class="d-flex flex-column-reverse mb-6 bg-surface-variant">
      <v-sheet class="ma-2 pa-2">Flex item 1</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item 2</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item 3</v-sheet>
    </div>
  </div>
</template>

```

# Vuetify concept flex - margins align items

Example code

```vue
<template>
  <div>
    <v-sheet
      class="d-flex align-start flex-column mb-6 bg-surface-variant"
      height="200"
    >
      <v-sheet class="ma-2 pa-2 mb-auto">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
    </v-sheet>

    <v-sheet
      class="d-flex align-end flex-column bg-surface-variant"
      height="200"
    >
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item</v-sheet>
      <v-sheet class="ma-2 pa-2 mt-auto">Flex item</v-sheet>
    </v-sheet>
  </div>
</template>

```

# Vuetify concept flex - flex align content around

Example code

```vue
<template>
  <v-sheet
    class="d-flex align-content-space-around flex-wrap bg-surface-variant"
    min-height="200"
  >
    <v-sheet
      v-for="n in 20"
      :key="n"
      class="ma-2 pa-2"
    >
      Flex item
    </v-sheet>
  </v-sheet>
</template>

```

# Vuetify concept flex - flexbox

Example code

```vue
<template>
  <v-sheet class="d-flex bg-surface-variant">
    <v-sheet class="ma-2 pa-2">
      I'm a single element in a flexbox container!
    </v-sheet>
  </v-sheet>
</template>

```

# Vuetify concept flex - flex justify

Example code

```vue
<template>
  <div>
    <div class="d-flex justify-start mb-6 bg-surface-variant">
      <v-sheet
        v-for="n in 3"
        :key="n"
        class="ma-2 pa-2"
      >
        justify-start
      </v-sheet>
    </div>

    <div class="d-flex justify-end mb-6 bg-surface-variant">
      <v-sheet
        v-for="n in 3"
        :key="n"
        class="ma-2 pa-2"
      >
        justify-end
      </v-sheet>
    </div>

    <div class="d-flex justify-center mb-6 bg-surface-variant">
      <v-sheet
        v-for="n in 3"
        :key="n"
        class="ma-2 pa-2"
      >
        justify-center
      </v-sheet>
    </div>

    <div class="d-flex justify-space-between mb-6 bg-surface-variant">
      <v-sheet
        v-for="n in 3"
        :key="n"
        class="ma-2 pa-2"
      >
        justify-space-between
      </v-sheet>
    </div>

    <div class="d-flex justify-space-around mb-6 bg-surface-variant">
      <v-sheet
        v-for="n in 3"
        :key="n"
        class="ma-2 pa-2"
      >
        justify-space-around
      </v-sheet>
    </div>

    <div class="d-flex justify-space-evenly mb-6 bg-surface-variant">
      <v-sheet
        v-for="n in 3"
        :key="n"
        class="ma-2 pa-2"
      >
        justify-space-evenly
      </v-sheet>
    </div>
  </div>
</template>

```

# Vuetify concept flex - flex order

Example code

```vue
<template>
  <v-sheet class="d-flex flex-wrap-reverse bg-surface-variant">
    <v-sheet class="order-3 pa-2 ma-2">
      First flex item
    </v-sheet>

    <v-sheet class="order-2 pa-2 ma-2">
      Second flex item
    </v-sheet>

    <v-sheet class="order-1 pa-2 ma-2">
      Third flex item
    </v-sheet>
  </v-sheet>
</template>

```

# Vuetify concept flex - flex align

Example code

```vue
<template>
  <div>
    <v-sheet
      class="d-flex align-start mb-6 bg-surface-variant"
      height="100"
    >
      <v-sheet
        v-for="n in 3"
        :key="n"
        class="ma-2 pa-2"
      >
        align-start
      </v-sheet>
    </v-sheet>

    <v-sheet
      class="d-flex align-end mb-6 bg-surface-variant"
      height="100"
    >
      <v-sheet
        v-for="n in 3"
        :key="n"
        class="ma-2 pa-2"
      >
        align-end
      </v-sheet>
    </v-sheet>

    <v-sheet
      class="d-flex align-center mb-6 bg-surface-variant"
      height="100"
    >
      <v-sheet
        v-for="n in 3"
        :key="n"
        class="ma-2 pa-2"
      >
        align-center
      </v-sheet>
    </v-sheet>

    <v-sheet
      class="d-flex align-baseline mb-6 bg-surface-variant"
      height="100"
    >
      <v-sheet
        v-for="n in 3"
        :key="n"
        class="ma-2 pa-2"
      >
        align-baseline
      </v-sheet>
    </v-sheet>

    <v-sheet
      class="d-flex align-stretch mb-6 bg-surface-variant"
      height="100"
    >
      <v-sheet
        v-for="n in 3"
        :key="n"
        class="ma-2 pa-2"
      >
        align-stretch
      </v-sheet>
    </v-sheet>
  </div>
</template>

```

# Vuetify concept flex - flex wrap

Example code

```vue
<template>
  <v-sheet class="d-flex flex-wrap bg-surface-variant">
    <v-sheet
      v-for="n in 20"
      :key="n"
      class="ma-2 pa-2"
    >
      Flex item {{ n }}
    </v-sheet>
  </v-sheet>
</template>

```

# Vuetify concept flex - flexbox inline

Example code

```vue
<template>
  <v-sheet class="d-inline-flex bg-surface-variant">
    <v-sheet class="ma-2 pa-2">
      I'm a single element in an inline flexbox container!
    </v-sheet>
  </v-sheet>
</template>

```

# Vuetify concept flex - flex align content between

Example code

```vue
<template>
  <v-sheet
    class="d-flex align-content-space-between flex-wrap bg-surface-variant"
    min-height="200"
  >
    <v-sheet
      v-for="n in 20"
      :key="n"
      class="ma-2 pa-2"
    >
      Flex item
    </v-sheet>
  </v-sheet>
</template>

```

# Vuetify concept flex - flex direction

Example code

```vue
<template>
  <div>
    <div class="d-flex flex-row mb-6 bg-surface-variant">
      <v-sheet class="ma-2 pa-2">Flex item 1</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item 2</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item 3</v-sheet>
    </div>

    <div class="d-flex flex-row-reverse mb-6 bg-surface-variant">
      <v-sheet class="ma-2 pa-2">Flex item 1</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item 2</v-sheet>
      <v-sheet class="ma-2 pa-2">Flex item 3</v-sheet>
    </div>
  </div>
</template>

```

# Vuetify concept flex - flex wrap reverse

Example code

```vue
<template>
  <v-sheet class="d-flex flex-wrap-reverse bg-surface-variant">
    <v-sheet
      v-for="n in 20"
      :key="n"
      class="ma-2 pa-2"
    >
      Flex item {{ n }}
    </v-sheet>
  </v-sheet>
</template>

```

# Vuetify concept flex - flex flex

Example code

```vue
<template>
  <v-sheet class="d-flex flex-wrap bg-surface-variant">
    <v-sheet class="flex-1-0 ma-2 pa-2">
      I'm an element in an inline flexbox container!
    </v-sheet>

    <v-sheet class="ma-2 pa-2">
      I'm a single element in an inline flexbox container!
    </v-sheet>

    <v-sheet class="flex-1-1-100 ma-2 pa-2">
      I'm a single element in an inline flexbox container!
    </v-sheet>
  </v-sheet>
</template>

```

# Vuetify concept flex - flex align content end

Example code

```vue
<template>
  <v-sheet
    class="d-flex align-content-end flex-wrap bg-surface-variant"
    min-height="200"
  >
    <v-sheet
      v-for="n in 20"
      :key="n"
      class="ma-2 pa-2"
    >
      Flex item
    </v-sheet>
  </v-sheet>
</template>

```

# Vuetify concept flex - flex align content start

Example code

```vue
<template>
  <v-sheet
    class="d-flex align-content-start flex-wrap bg-surface-variant"
    min-height="200"
  >
    <v-sheet
      v-for="n in 20"
      :key="n"
      class="ma-2 pa-2"
    >
      Flex item
    </v-sheet>
  </v-sheet>
</template>

```
