# Created by dima at 30.10.18
Feature: Pick origin photos matched to chosen google photo album
  In order to review photos from album in good quality on TV
  As a person who likes great pictures
  I want to save pictures from the album in original quality at separate folder

  Scenario: Save photos included in album to destination folder in original quality
    Given I set name of google photo album
    And I set destination folder
    And I set path ot original photos
    When I make request
    Then I see all album photos at destination folder in original quality