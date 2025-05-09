# Vuetify component v-img - usage

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
      <v-img
        v-bind="props"
        :aspect-ratio="aspectRatio.value"
        class="mx-auto"
      ></v-img>
    </div>

    <template v-slot:configuration>

      <v-select
        v-model="aspectRatio"
        :items="aspectRatios"
        label="Aspect ratio"
        return-object
      ></v-select>

      <v-slider
        v-model="width"
        label="Width"
        max="400"
        min="100"
      ></v-slider>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-img'
  const model = ref('default')
  const width = ref(300)
  const aspectRatio = ref({ title: '16/9', value: 16 / 9 })
  const aspectRatios = [
    { title: '16/9', value: 16 / 9 },
    { title: '4/3', value: 4 / 3 },
    { title: '1/1', value: 1 },
  ]
  const options = []

  const props = computed(() => {
    return {
      width: width.value,
      'aspect-ratio': aspectRatio.value.title,
      cover: true,
      src: 'https://cdn.vuetifyjs.com/images/parallax/material.jpg',
    }
  })

  const slots = computed(() => {
    return ''
  })

  const code = computed(() => {
    return `<v-img${propsToString(props.value)}>${slots.value}</v-img>`
  })
</script>

```

# Vuetify component v-img - prop max height

Example code

```vue
<template>
  <v-container
    class="fill-height"
    style="min-height: 434px"
    fluid
  >
    <v-fade-transition mode="out-in">
      <v-row>
        <v-col cols="6">
          <v-card>
            <v-img
              class="bg-grey-lighten-2"
              height="125"
              src="https://picsum.photos/350/165?random"
            ></v-img>
            <v-card-title class="text-h6">
              height
            </v-card-title>
          </v-card>
        </v-col>

        <v-col cols="6">
          <v-card>
            <v-img
              class="bg-grey-lighten-2"
              height="125"
              src="https://picsum.photos/350/165?random"
              cover
            ></v-img>
            <v-card-title class="text-h6">
              height with cover
            </v-card-title>
          </v-card>
        </v-col>

        <v-col cols="6">
          <v-card>
            <v-img
              class="bg-grey-lighten-2"
              max-height="125"
              src="https://picsum.photos/350/165?random"
            ></v-img>
            <v-card-title class="text-h6">
              max-height
            </v-card-title>
          </v-card>
        </v-col>

        <v-col cols="6">
          <v-card>
            <v-img
              class="bg-grey-lighten-2"
              max-height="125"
              src="https://picsum.photos/350/165?random"
              cover
            ></v-img>
            <v-card-title class="text-h6">
              max-height with cover
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-fade-transition>
  </v-container>
</template>

```

# Vuetify component v-img - misc grid

Example code

```vue
<template>
  <v-row>
    <v-col
      v-for="n in 9"
      :key="n"
      class="d-flex child-flex"
      cols="4"
    >
      <v-img
        :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
        :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
        aspect-ratio="1"
        class="bg-grey-lighten-2"
        cover
      >
        <template v-slot:placeholder>
          <v-row
            align="center"
            class="fill-height ma-0"
            justify="center"
          >
            <v-progress-circular
              color="grey-lighten-5"
              indeterminate
            ></v-progress-circular>
          </v-row>
        </template>
      </v-img>
    </v-col>
  </v-row>
</template>

```

# Vuetify component v-img - complex grid

Example code

```vue
<template>
  <v-row>
    <template v-for="(image,imgIdx) in imageLayout" :key="imgIdx">
      <v-col :cols="image.cols">
        <v-img
          :src="`https://picsum.photos/500/300?image=${image.cols * 20}`"
          height="100%"
          cover
        ></v-img>
      </v-col>

      <v-col v-if="image.children" class="d-flex flex-column" cols="6">
        <v-row>
          <v-col v-for="(children,childIdx) in image.children" :key="childIdx" :cols="children.cols">
            <v-img
              :src="`https://picsum.photos/500/300?image=${children.cols + childIdx}`"
              height="100%"
              cover
            ></v-img>
          </v-col>
        </v-row>
      </v-col>
    </template>
  </v-row>
</template>

<script setup>
  const imageLayout = [
    { cols: 4 },
    {
      cols: 8,
      children: [{ cols: 12 }, { cols: 12 }],
    },
    { cols: 6 },
    { cols: 3 },
    { cols: 9 },
    { cols: 4 },
    { cols: 8 },
  ]
</script>

```

# Vuetify component v-img - slot placeholder

Example code

```vue
<template>
  <v-img
    class="mx-auto"
    height="300"
    lazy-src="https://picsum.photos/id/11/100/60"
    max-width="500"
    src="https://bad.src/not/valid"
  >
    <template v-slot:placeholder>
      <div class="d-flex align-center justify-center fill-height">
        <v-progress-circular
          color="grey-lighten-4"
          indeterminate
        ></v-progress-circular>
      </div>
    </template>
  </v-img>
</template>

```

# Vuetify component v-img - slot error

Example code

```vue
<template>
  <v-img
    class="mx-auto"
    height="300"
    max-width="500"
    src="https://bad.src/not/valid"
  >
    <template v-slot:error>
      <v-img
        class="mx-auto"
        height="300"
        max-width="500"
        src="https://picsum.photos/500/300?image=232"
      ></v-img>
    </template>
  </v-img>
</template>

```

# Vuetify component v-img - prop cover

Example code

```vue
<template>
  <div class="d-flex justify-space-around align-center bg-grey-lighten-4">
    <div class="ma-4">
      <div class="text-subtitle-2">Default</div>
      <v-img
        :aspect-ratio="1"
        class="bg-white"
        src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
        width="300"
      ></v-img>
    </div>

    <div class="ma-4">
      <div class="text-subtitle-2">Cover</div>
      <v-img
        :aspect-ratio="1"
        class="bg-white"
        src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
        width="300"
        cover
      ></v-img>
    </div>
  </div>
</template>

```

# Vuetify component v-img - prop contain

Example code

```vue
<template>
  <v-container fluid>
    <v-row justify="space-around">
      <v-col cols="5">
        <div class="text-h6 mb-1">
          Default (cover)
        </div>
        <div class="subheading">
          Matching
        </div>
        <v-img
          aspect-ratio="1.7"
          src="https://picsum.photos/510/300?random"
        ></v-img>
        <div class="subheading pt-4">
          Too high
        </div>
        <v-img
          aspect-ratio="2"
          src="https://picsum.photos/510/300?random"
        ></v-img>
        <div class="subheading pt-4">
          Too low
        </div>
        <v-img
          aspect-ratio="1.4"
          src="https://picsum.photos/510/300?random"
        ></v-img>
      </v-col>

      <v-col cols="5">
        <div class="text-h6 mb-1">
          Contain
        </div>
        <div class="subheading">
          Matching
        </div>
        <v-img
          aspect-ratio="1.7"
          src="https://picsum.photos/510/300?random"
        ></v-img>
        <div class="subheading pt-4">
          Too high
        </div>
        <v-img
          aspect-ratio="2"
          src="https://picsum.photos/510/300?random"
        ></v-img>
        <div class="subheading pt-4">
          Too low
        </div>
        <v-img
          aspect-ratio="1.4"
          src="https://picsum.photos/510/300?random"
        ></v-img>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-img - prop gradient

Example code

```vue
<template>
  <v-row>
    <v-col
      cols="6"
      sm="4"
    >
      <v-img
        gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
        src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"
      ></v-img>
    </v-col>

    <v-col
      cols="6"
      sm="4"
    >
      <v-img src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg">
        <div class="fill-height bottom-gradient"></div>
      </v-img>
    </v-col>

    <v-col
      cols="6"
      sm="4"
    >
      <v-img src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg">
        <div class="fill-height repeating-gradient"></div>
      </v-img>
    </v-col>
  </v-row>
</template>

<style scoped>
  .bottom-gradient {
    background-image: linear-gradient(to top, rgba(0, 0, 0, 0.4) 0%, transparent 72px);
  }

  .repeating-gradient {
    background-image: repeating-linear-gradient(-45deg,
                        rgba(255,0,0,.25),
                        rgba(255,0,0,.25) 5px,
                        rgba(0,0,255,.25) 5px,
                        rgba(0,0,255,.25) 10px
                      );
  }
</style>

```
