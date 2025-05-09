# Vuetify concept concepts - density

Example code

```vue
<template>
  <v-container class="pa-2">
    <v-row>
      <v-col cols="12">
        <v-label class="d-block mb-4">Density Scale</v-label>

        <v-btn-toggle
          v-model="density"
          class="overflow-auto"
          color="primary"
          density="compact"
          variant="outlined"
          divided
        >
          <v-btn text="Default" value="default"></v-btn>

          <v-btn text="Comfortable" value="comfortable"></v-btn>

          <v-btn text="Compact" value="compact"></v-btn>
        </v-btn-toggle>
      </v-col>

      <v-divider class="flex-grow-1 mt-1 mx-n1"></v-divider>

      <v-col cols="12">
        <v-list-subheader>Buttons</v-list-subheader>

        <v-btn
          :density="density"
          class="me-2 mb-2"
          text="Submit"
        ></v-btn>

        <v-btn
          :density="density"
          class="me-2 mb-2"
          text="Load More"
          variant="text"
        ></v-btn>

        <v-btn
          :density="density"
          class="me-2 mb-2"
          text="Cancel"
          variant="outlined"
        ></v-btn>
      </v-col>

      <v-col cols="12">
        <v-list-subheader>Chips</v-list-subheader>

        <v-chip
          :density="density"
          class="me-2 mb-2"
          text="In Progress"
        ></v-chip>

        <v-chip
          :density="density"
          class="me-2 mb-2"
          text="High Priority"
        ></v-chip>

        <v-chip
          :density="density"
          class="me-2 mb-2"
          text="Assigned"
        ></v-chip>
      </v-col>

      <v-col cols="12">
        <v-list-subheader>Toolbars</v-list-subheader>

        <v-toolbar
          :density="density"
          class="mb-2"
          elevation="2"
          title="Daily Reports"
        ></v-toolbar>

        <v-toolbar
          :density="density"
          class="mb-2"
          title="User Dashboard"
        ></v-toolbar>

        <v-toolbar
          :density="density"
          color="transparent"
          title="Project Settings"
          border
        ></v-toolbar>
      </v-col>

      <v-col cols="12">
        <v-list-subheader>Text Fields</v-list-subheader>

        <v-text-field
          :density="density"
          label="Search Query"
          model-value="Data tables"
          prepend-inner-icon="mdi-magnify"
          variant="solo"
        ></v-text-field>

        <v-text-field
          :density="density"
          label="Email Address"
          model-value="hello@vuetifyjs.com"
          prepend-inner-icon="mdi-email-outline"
        ></v-text-field>

        <v-text-field
          :density="density"
          label="Username"
          model-value="John Leider"
          prepend-inner-icon="mdi-account-outline"
          variant="outlined"
          hide-details
        ></v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const density = shallowRef('default')
</script>

```

# Vuetify concept concepts - density and size

Example code

```vue
<template>
  <v-container class="pa-4">
    <v-row>
      <v-col cols="12" md="6">
        <v-slider
          v-model="size"
          class="pt-6"
          label="Size"
          max="4"
          min="0"
          step="1"
          thumb-label="always"
          hide-details
        >
          <template v-slot:thumb-label="{ modelValue }">
            <div class="text-no-wrap">
              {{ sizes[modelValue] }}
            </div>
          </template>
        </v-slider>
      </v-col>

      <v-col cols="12" md="6">
        <v-slider
          v-model="density"
          class="pt-6"
          label="Density"
          max="2"
          min="0"
          step="1"
          thumb-label="always"
          hide-details
        >
          <template v-slot:thumb-label="{ modelValue }">
            <div class="text-no-wrap">
              {{ densities[modelValue] }}
            </div>
          </template>
        </v-slider>
      </v-col>

      <v-divider class="flex-grow-1 my-2 mx-n1"></v-divider>

      <v-col cols="12">
        <v-list-subheader>Buttons</v-list-subheader>

        <v-btn
          :density="densities[density]"
          :size="sizes[size]"
          class="me-2 mb-2"
          prepend-icon="$vuetify"
          text="Default Button"
        ></v-btn>

        <v-btn
          :density="densities[density]"
          :size="sizes[size]"
          append-icon="mdi-account-outline"
          class="me-2 mb-2"
          text="User Profile"
          variant="tonal"
        ></v-btn>

        <v-btn
          :density="densities[density]"
          :size="sizes[size]"
          class="me-2 mb-2"
          icon="$vuetify"
        ></v-btn>
      </v-col>

      <v-col cols="12">
        <v-list-subheader>Chips</v-list-subheader>

        <v-chip
          :density="densities[density]"
          :size="sizes[size]"
          class="me-2 mb-2"

          text="Complete"
        ></v-chip>

        <v-chip
          :density="densities[density]"
          :size="sizes[size]"
          class="me-2 mb-2"
          text="Reset"
          variant="outlined"
        ></v-chip>

        <v-chip
          :density="densities[density]"
          :size="sizes[size]"
          class="me-2 mb-2"
          text="Disabled"
          disabled
        ></v-chip>
      </v-col>

      <v-col cols="12">
        <v-list-subheader>Avatars</v-list-subheader>

        <v-avatar
          :density="densities[density]"
          :size="sizes[size]"
          color="surface-variant"
          image="https://cdn.vuetifyjs.com/docs/images/avatars/grass.png"
        ></v-avatar>

        <v-avatar
          :density="densities[density]"
          :size="sizes[size]"
          class="ms-2"
          image="https://cdn.vuetifyjs.com/docs/images/avatars/gold.png"
        ></v-avatar>

        <v-avatar
          :density="densities[density]"
          :size="sizes[size]"
          class="ms-2"
          color="surface-variant"
          image="https://cdn.vuetifyjs.com/docs/images/avatars/planet.png"
        ></v-avatar>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const size = shallowRef(2)
  const density = shallowRef(2)

  const densities = ['compact', 'comfortable', 'default']
  const sizes = ['x-small', 'small', 'default', 'large', 'x-large']
</script>

```

# Vuetify concept concepts - size

Example code

```vue
<template>
  <v-container class="pa-2">
    <v-row>
      <v-col cols="12">
        <v-label class="d-block mb-4">Size Scale</v-label>

        <v-btn-toggle
          v-model="size"
          class="overflow-auto"
          color="primary"
          density="compact"
          direction="vertical"
          variant="outlined"
          divided
        >
          <v-btn text="X-small" value="x-small"></v-btn>

          <v-btn text="Small" value="small"></v-btn>

          <v-btn text="Default" value="default"></v-btn>

          <v-btn text="Large" value="large"></v-btn>

          <v-btn text="x-large" value="x-large"></v-btn>
        </v-btn-toggle>
      </v-col>

      <v-divider class="flex-grow-1 my-2 mx-n1"></v-divider>

      <v-col cols="12">
        <v-list-subheader>Buttons</v-list-subheader>

        <v-btn
          :size="size"
          class="me-2 mb-2"
          text="Export"
        ></v-btn>

        <v-btn
          :size="size"
          class="me-2 mb-2"
          text="Edit"
          variant="text"
        ></v-btn>

        <v-btn
          :size="size"
          class="me-2 mb-2"
          text="Preview"
          variant="outlined"
        ></v-btn>
      </v-col>

      <v-col cols="12">
        <v-list-subheader>Chips</v-list-subheader>

        <v-chip
          :size="size"
          class="me-2 mb-2"
          text="Completed"
        ></v-chip>

        <v-chip
          :size="size"
          class="me-2 mb-2"
          text="Archived"
        ></v-chip>

        <v-chip
          :size="size"
          class="me-2 mb-2"
          text="New"
        ></v-chip>
      </v-col>

      <v-col cols="12">
        <v-list-subheader>Ratings</v-list-subheader>

        <v-rating
          :size="size"
          label="Customer Satisfaction"
          length="3"
        ></v-rating>

        <br>

        <v-rating
          :size="size"
          label="Ease of Use"
          length="4"
        ></v-rating>

        <br>

        <v-rating
          :size="size"
          label="Quality"
        ></v-rating>
      </v-col>

      <v-col cols="12">
        <v-list-subheader>Avatars</v-list-subheader>

        <v-avatar
          :size="size"
          class="mb-2 me-2"
          image="https://cdn.vuetifyjs.com/docs/images/avatars/dark.png"
        ></v-avatar>

        <v-avatar
          :size="size"
          class="mb-2 me-2"
          image="https://cdn.vuetifyjs.com/docs/images/avatars/blackhole.png"
        ></v-avatar>

        <v-avatar
          :size="size"
          class="mb-2 me-2"
          image="https://cdn.vuetifyjs.com/docs/images/avatars/meteor.png"
        ></v-avatar>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const size = shallowRef('default')
</script>

```
