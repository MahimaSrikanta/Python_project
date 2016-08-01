var app = angular.module("myApp", []);
app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');
}]);

app.controller("myCtrl", function($scope) {

  $scope.toggleSibling = function($event){

    console.log($event.target.id);
    if ($event.target.id == "events"){
      $scope.even = [];


      $scope.mergedLists = {};

      {%for events in city_value['City_events']%}
        $scope.even.push({'name':'{{events[0]}}', 'date':'{{events[1]}}','addr':'{{events[2]}}'} ); // Gets the event name
      {% endfor %}



    console.log($scope.even);


  }
  if ($event.target.id == "Places"){
    $scope.even = [];
    {%for events in city_value['City_places']%}
      $scope.even.push({'name':'{{events[0]}}', 'date':'{{events[1]}}','addr':'{{events[2]}}'} ); // Gets the event name
    {% endfor %}
  console.log($scope.even);

}
if ($event.target.id == "Hotels"){
  $scope.even = [];
  {%for events in city_value['City_hotels']%}
$scope.even.push({'name':'{{events[0]}}', 'date':'{{events[1]}}','addr':'{{events[2]}}'} ); // Gets the event name

{% endfor %}

}
if ($event.target.id == "resturants"){
$scope.even = [];

{%for events in city_value['City_resturants']%}
  $scope.even.push({'name':'{{events[0]}}', 'date':'{{events[1]}}','addr':'{{events[2]}}'} ); // Gets the event name
{% endfor %}


}
}
});
