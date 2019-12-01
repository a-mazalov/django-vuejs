<template>
	<v-container style="margin-top: 60px;" fill-height>
		<v-container class="mb-0" fill-height>
			<v-row justify="center" align="center" no-gutters>
				<v-col>
					<div>
						<h1 class="display-3 text-center">
							{{ course.name }}
							<v-icon x-large :color="coloredIcons(course.direction)">mdi-language-{{course.direction}}</v-icon>
						</h1>
					</div>
					<v-card outlined class="mt-10 pa-5">
						<!-- <v-card-text> -->
						<v-row no-gutters>
							<div>
								<v-icon large class="mr-2 pb-2" color="orange">mdi-account-star</v-icon>
								<span class="subtitle-1">Уровень: <b>{{ course.level }}</b></span>
							</div>
							<v-spacer></v-spacer>
							<div>
								<v-icon large color="primary" class="mr-2 pb-2">mdi-calendar-edit</v-icon>
								<span
									class="subtitle-1"
								>Начало регистрации: {{ $moment(course.date_start_registration).format('Do MMMM') }}</span>
							</div>
						</v-row>


						<div class="my-10">
							<v-icon large class="mr-2 pb-2" >mdi-book</v-icon>
							<span class="subtitle-1">Описание: </span>
							<blockquote class="blockquote">{{ course.description }}</blockquote>
						</div>
						<div class="">
							<v-icon large class="mr-2 pb-2">mdi-progress-clock</v-icon>
							<span class="subtitle-1">Продолжительность: <b>{{ course.duration }}ч.</b></span>
						</div>
						<div >
							<v-icon large class="mr-2 pb-2" color="primary">mdi-update</v-icon>
							<span class="subtitle-1">Дата старта: {{ $moment(course.date_start).format('Do MMMM') }}</span>
						</div>

						<!-- </v-card-text> -->

						<v-card-actions>
							<v-spacer></v-spacer>
							<v-btn text @click="unFollowCourse(course.id)" color="secondary">Отписаться</v-btn>
							<v-btn @click="followCourse(course.id)" color="primary">Участвовать</v-btn>
						</v-card-actions>
					</v-card>

					<!-- <v-divider width="350px"></v-divider> -->
				</v-col>
				<v-col class="d-flex justify-end">
					<v-img src="../assets/advance_feature_img.png" max-width="400" contain></v-img>
				</v-col>
				<!-- <v-col cols="12"> -->
				<!-- </v-col> -->
			</v-row>
		</v-container>
	</v-container>
</template>

<script>
	import { mapState, mapActions } from "vuex";
	import auth from "../api/auth";

	export default {
		name: "Courses",
		data() {
			return {
				subject: "",
				msgBody: "",
				user: null
			};
		},
		computed: {
			...mapState({
				course: function(state) {
					return state.courses.courses.find(
						obj => obj.id == this.$route.params.id
					);
				}
			})
		},
		methods: {
			...mapActions("courses", ["addCourse", "deleteCourse"]),

			followCourse(crsId) {
				this.$store.dispatch("courses/joinCourse", crsId);
			},
			unFollowCourse(crsId) {
				this.$store.dispatch("courses/outCourse", crsId);
			},

			coloredIcons(language) {
				let color = "grey";

				switch (language) {
					case "javascript":
						color = "orange";
						break;
					case "python":
						color = "primary";
						break;
					case "php":
						color = "deep-purple lighten-1";
						break;
				}

				return color;
			}
		},

		created() {
			// this.course = courses.filter(obj => obj.id == this.$route.params)

			// auth.getAccountDetails().then(response =>
			// 	this.user = response.data
			// )

			this.$store.dispatch("courses/getCourses");
			// console.log(
			// 	this.$store.state.courses.courses.filter(
			// 		obj => obj.id == this.$route.params.id
			// 	)
			// );
		}
	};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	hr {
		max-width: 65%;
	}

	.msg {
		margin: 0 auto;
		max-width: 30%;
		text-align: left;
		border-bottom: 1px solid #ccc;
		padding: 1rem;
	}

	.msg-index {
		color: #ccc;
		font-size: 0.8rem;
		/* margin-bottom: 0; */
	}

	img {
		width: 250px;
		padding-top: 50px;
		padding-bottom: 50px;
	}
</style>
