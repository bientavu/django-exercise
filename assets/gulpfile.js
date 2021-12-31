var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var sourcemaps = require('gulp-sourcemaps');
var notify = require("gulp-notify");
var postcss = require("gulp-postcss");
var autoprefixer = require('autoprefixer');
var livereload = require('gulp-livereload');

gulp.task('styles', function() {
  return gulp.src('scss/*.scss')
    .pipe(sourcemaps.init())
    .pipe(sass({
        outputStyle: 'compressed'
    }).on('error', sass.logError))
    .pipe(postcss([
      autoprefixer({
        remove: false,
      })
    ]))
    .pipe(sourcemaps.write("./"))
    .pipe(gulp.dest('./css'))
    .pipe(notify("CSS generated"))
    .pipe(livereload());
});

gulp.task('scripts', function() {
  return gulp.src([
      'js/variables.js',
      'js/init.js',
      'js/utils.js',
      'js/cookies.js',
      'js/to-show.js',
      'js/async.js',
      'js/carousels.js',
      'js/scroll-to.js',
      'js/animations.js',
    ])
    .pipe(sourcemaps.init())
    .pipe(concat('main.js'))
    .pipe(gulp.dest('js'))
    .pipe(uglify())
    .pipe(rename({ extname: '.min.js' }))
    .pipe(sourcemaps.write("./"))
    .pipe(gulp.dest('js'))
    .on('error', sass.logError)
    .pipe(notify("JS generated"))
    .pipe(livereload());
});

gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('scss/**', ['styles']);
    gulp.watch('js/**', ['scripts']);
});

gulp.task('default', ['watch']);
