module Main exposing (..)

import Html exposing (Html, div, text)


-- MODEL


type alias Model =
    { x : Int
    , y : Int
    }



-- MESSAGE


type Msg
    = NoOp



-- INIT


init : ( Model, Cmd Msg )
init =
    ( Model 0 0
    , Cmd.none
    )



-- UPDATE


update : Msg -> Model -> ( Model, Cmd Msg )
update message model =
    ( model, Cmd.none )



-- VIEW


view : Model -> Html Msg
view model =
    div []
        [ text "Hello World" ]



-- SUBSCRIPTIONS


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none



-- MAIN


main : Program Never Model Msg
main =
    Html.program
        { init = init
        , subscriptions = subscriptions
        , update = update
        , view = view
        }
