<template>
	<!-- <div id="register-view">
		<h1>Create Account</h1>
		<template v-if="registrationLoading">loading...</template>
		<template v-else-if="!registrationCompleted">
			<form @submit.prevent="submit">
				<input v-model="inputs.username" type="text" id="username" placeholder="username" />
				<input v-model="inputs.password1" type="password" id="password1" placeholder="password" />
				<input v-model="inputs.password2" type="password" id="password2" placeholder="confirm password" />
				<input v-model="inputs.email" type="email" id="email" placeholder="email" />
			</form>
			<button @click="createAccount(inputs)">create account</button>
			<span class="error" v-show="registrationError">An error occured while processing your request.</span>
			<div>
				Already have an account?
				<router-link to="/login">login</router-link>|
				<router-link to="/password_reset">reset password</router-link>
			</div>
		</template>
		<template v-else>
			<div>
				Registration complete. You should receive an email shortly with instructions on how to
				activate your account.
			</div>
			<div>
				<router-link to="/login">return to login page</router-link>
			</div>
		</template>
	</div>-->
	<v-container fill-height class="register-page">
		<v-row align="center">
			<v-col md="6" sm="6" xs="12">
				<div class="text-center">
					<h1 class="display-1">Хочешь научиться программировать?</h1>
					<h3 class="font-weight-light">Получи доступ к десяткам бесплатных материалов</h3>
					<h3 class="font-weight-light">Общайся и учись у ведущих IT-специалистов</h3>
				</div>
			</v-col>
			<v-col md="6" sm="6" xs="12">
				<div v-if="!registrationCompleted">
					<h4 class="text-center headline my-4">Регистрация аккаунта</h4>
					<v-card class="mx-auto" max-width="480" shaped :elevation="5" :loading="registrationLoading">
						<div class="pa-5">
							<v-card-text>
								<v-form ref="form" v-model="valid">
									<v-text-field
										outlined
										v-model="inputs.username"
										type="text"
										id="username"
										label="Логин"
										prepend-inner-icon="fa-user"
										required
									></v-text-field>
									<v-text-field
										outlined
										v-model="inputs.password1"
										id="password"
										label="Пароль"
										required
										prepend-inner-icon="fa-lock"
										:type="showPassword1 ? 'text' : 'password'"
										:append-icon="showPassword1 ? 'fa-eye' : 'fa-eye-slash'"
										@click:append="showPassword1 = !showPassword1"
									></v-text-field>
									<v-text-field
										outlined
										v-model="inputs.password2"
										id="password2"
										label="Подтвердите пароль"
										required
										prepend-inner-icon="fa-lock"
										:type="showPassword2 ? 'text' : 'password'"
										:append-icon="showPassword2 ? 'fa-eye' : 'fa-eye-slash'"
										@click:append="showPassword2 = !showPassword2"
									></v-text-field>
									<v-text-field
										outlined
										v-model="inputs.email"
										type="text"
										id="email"
										label="E-mail"
										prepend-inner-icon="fa-at"
										required
									></v-text-field>

									<div class="text-right">
										<v-breadcrumbs :items="urls" class="justify-end pa-0"></v-breadcrumbs>
									</div>

									<v-checkbox
										v-model="inputs.checkbox"
										label="Подтверждаю, что ознакомлен и принимаю условия"
										required
									></v-checkbox>
								</v-form>
								<v-alert v-if="registrationError" type="error">Ошибка во время регистрации</v-alert>
							</v-card-text>
							<v-card-actions>
								<v-btn large block color="primary" @click="createAccount(inputs)">Зарегистрироваться</v-btn>
							</v-card-actions>
						</div>
					</v-card>
				</div>
				<div v-if="registrationCompleted">
					<h4 class="text-center headline my-4">Успешно зарегистрированы!</h4>
					<v-card class="mx-auto" max-width="480" shaped :elevation="5">
						<div class="pa-5">
							<v-card-text>
								Registration complete. You should receive an email shortly with instructions on how to
								activate your account.
							</v-card-text>
							<v-card-actions>
								<v-btn large block color="green" dark link to="/login">Перейти на главную</v-btn>
							</v-card-actions>
						</div>
					</v-card>
				</div>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
	data() {
		return {
			showPassword1: false,
			showPassword2: false,
			inputs: {
				username: "",
				password1: "",
				password2: "",
				email: ""
			},
			urls: [
				{
					text: "Войти",
					to: "/login"
				},
				{
					text: "Забыл пароль?",
					to: "/password_reset"
				}
			]
		};
	},
	computed: mapState("signup", [
		"registrationCompleted",
		"registrationError",
		"registrationLoading"
	]),
	methods: mapActions("signup", ["createAccount", "clearRegistrationStatus"]),
	beforeRouteLeave(to, from, next) {
		this.clearRegistrationStatus();
		next();
	}
};
</script>

<style>
.error {
	color: crimson;
	font-size: 12px;
}
.v-input__icon .v-icon.v-icon {
	font-size: 16px;
}
</style>
