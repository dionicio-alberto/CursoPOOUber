<?php
    require_once('payment.php');
    class Card extends Payment {
        public $number;
        public $cvv;
        public $date;

        public function __construct($id, $number, $cvv, $date){
            parent::__construct($id);
            $this->number = $number;
            $this->cvv = $cvv;
            $this->date = $date;
        }

        public function printDataCard(){
            echo "Number: $this->number , CVV:  $this->cvv , Date: $this->date";
        }
    }
?>
