# Vuetify concept position - static

Example code

```vue
<template>
  <div class="bg-surface-variant pa-4 position-relative rounded-lg ma-2">
    <div class="bg-surface-light position-static pa-3 pb-16">
      <div class="mb-2">Static parent</div>

      <div class="position-absolute bottom-0 right-0 bg-primary rounded-lg pa-3">
        Absolute child
      </div>
    </div>
  </div>
</template>

```

# Vuetify concept position - absolute

Example code

```vue
<template>
  <div class="text-caption px-4 mb-2">With static child</div>

  <div class="bg-surface-variant pa-4 position-relative rounded-lg mx-2 mb-2">
    <div class="mb-2">Relative parent</div>

    <div class="bg-surface-light position-static pa-3">
      <div class="mb-2">Static parent</div>

      <div class="position-static bg-primary rounded-lg pa-3 d-inline-block me-2">
        Static child
      </div>

      <div class="position-static bg-blue rounded-lg pa-3 d-inline-block">
        Static sibling
      </div>
    </div>
  </div>

  <div class="text-caption px-4 mb-2">With absolute child</div>

  <div class="bg-surface-variant pa-4 position-relative rounded-lg mx-2 mb-2">
    <div class="mb-2">Relative parent</div>

    <div class="bg-surface-light position-static pa-3">
      <div class="mb-3">Static parent</div>

      <div class="position-absolute top-0 right-0 bg-primary rounded-lg pa-3 d-inline-block">
        Absolute child
      </div>

      <div class="position-static bg-blue rounded-lg pa-3 d-inline-block">
        Static sibling
      </div>
    </div>
  </div>
</template>

```

# Vuetify concept position - relative

Example code

```vue
<template>
  <div class="bg-surface-variant pa-4 position-relative rounded-lg ma-2">
    <div class="bg-surface-light position-relative pa-3 pb-16">
      <div class="mb-2">Relative parent</div>

      <div class="position-absolute bottom-0 right-0 bg-primary rounded-lg pa-3">
        Absolute child
      </div>
    </div>
  </div>
</template>

```

# Vuetify concept position - sticky

Example code

```vue
<template>
  <div class="bg-surface-variant pa-4 position-relative rounded-lg ma-2">
    <div class="bg-surface-light position-relative py-3 ps-3">
      <div class="overflow-y-auto pe-3" style="max-height: 250px">
        <div>Relative parent</div>

        <div
          v-for="n in 5"
          :key="n"
        >
          <div class="bg-primary position-sticky top-0 pa-3 mt-2">
            Sticky header {{ n }}
          </div>

          <div
            v-for="k in 8"
            :key="k"
            class="bg-info rounded-lg pa-3 mt-2"
          >
            Static child
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

```

# Vuetify concept position - fixed

Example code

```vue
<template>
  <div class="bg-surface-variant pa-4 position-relative rounded-lg ma-2">
    <div class="bg-surface-light position-relative py-3 ps-3">
      <!-- position-absolute used for demonstration purposes -->
      <div class="position-absolute top-0 left-0 right-0 bg-primary pa-3 w-100">
        Fixed child
      </div>

      <div class="overflow-y-auto pe-3" style="max-height: 250px">
        <div class="mt-12">Relative parent</div>

        <div
          v-for="n in 10"
          :key="n"
          class="bg-info rounded-lg pa-3 mt-2"
        >
          Static child
        </div>
      </div>
    </div>
  </div>
</template>

```
