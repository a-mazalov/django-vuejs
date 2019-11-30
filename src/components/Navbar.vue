<template>
	<v-app-bar app flat class="px-5" color="transparent">
		<v-btn icon link to="/">
			<v-icon>fa-graduation-cap</v-icon>
		</v-btn>

		<v-toolbar-title>Главная</v-toolbar-title>

		<v-spacer></v-spacer>

		<v-btn icon link to="/about">
			<v-icon>fa-address-card</v-icon>
		</v-btn>
		<v-btn icon link to="/logout">
			<v-icon>fa-sign-out-alt</v-icon>
		</v-btn>
	</v-app-bar>
</template>

<script>
	export default {
		name: "navbar"
	};
</script>

<style scoped>
</style>
