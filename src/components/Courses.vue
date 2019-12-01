<template>
	<v-container style="margin-top: 60px;">
		<v-container class="mb-0">
			<v-row justify="center" align="center" no-gutters>
				<v-col>
					<div>
						<h1 class="display-3">Доступные курсы {{ user.username }}</h1>
						<!-- <v-divider width="350px"></v-divider> -->
					</div>
				</v-col>
				<v-col class="d-flex justify-end">
					<v-img
						src="https://colorlib.com/preview/theme/etrain/img/learning_img.png"
						max-width="500"
						contain
					></v-img>
				</v-col>
				<!-- <v-col cols="12"> -->
				<!-- </v-col> -->
			</v-row>
			<v-row class="mt-1">
				<v-divider style="max-width:100%"></v-divider>
			</v-row>
		</v-container>
		
		<v-container>
			<v-row justify="start" align="start">
				<!-- {{ courses }} -->
				<v-col cols="12" sm="6" md="6" lg="4" v-for="course in courses" :key="course.id">
					<v-card>
						<v-list-item three-line>
							<v-list-item-content>
								<div class="caption mb-4">{{ $moment(course.created).format('DD.MM.YYYY') }}</div>
								<v-list-item-title class="headline mb-2">{{ course.name }}</v-list-item-title>
							</v-list-item-content>

							<v-list-item-avatar size="80">
								<v-icon x-large :color="coloredIcons(course.direction)">mdi-language-{{course.direction}}</v-icon>
							</v-list-item-avatar>
						</v-list-item>

						<v-card-text>
							<div>
								<v-icon class="mr-2">mdi-account-star</v-icon>
								<span class="body-1">Уровень: {{ course.level }}</span>
							</div>
							<div>
								<v-icon class="mr-2">mdi-update</v-icon>
								<span class="body-1">Дата старта: {{ $moment(course.date_start).format('Do MMMM') }}</span>
							</div>
						</v-card-text>

						<v-card-actions>
							<v-btn text outlined link :to="'courses/'+course.id">Подробнее</v-btn>
							<v-spacer></v-spacer>
							<v-btn text @click="followCourse(course.id)" color="primary">Участвовать</v-btn>
							<v-btn text @click="unFollowCourse(course.id)" color="secondary">Отписаться</v-btn>
						</v-card-actions>
					</v-card>
				</v-col>
			</v-row>
		</v-container>
	</v-container>
</template>

<script>
	import { mapState, mapActions } from "vuex";
	import auth from '../api/auth';

	export default {
		name: "Courses",
		data() {
			return {
				subject: "",
				msgBody: "",
				user: null,
			};
		},
		computed: {
			...mapState({
				courses: state => state.courses.courses
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

			auth.getAccountDetails().then(response =>
				this.user = response.data
			)
			this.$store.dispatch("courses/getCourses");
			console.log(this.courses);
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
