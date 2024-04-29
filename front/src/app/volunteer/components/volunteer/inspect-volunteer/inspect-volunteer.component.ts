import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Volunteer } from 'src/app/shared/models/volunteer/volunteer.model';
import { DeleteVolunteerComponent } from '../delete-volunteer/delete-volunteer.component';
import { EditVolunteerComponent } from '../edit-volunteer/edit-volunteer.component';
import { ActivatedRoute, Router } from '@angular/router';
import { SwalFacade, VolunteerService } from 'src/app/shared';
import { Groups_id } from 'src/app/shared/models/volunteer';




@Component({
  selector: 'app-inspect-volunteer',
  templateUrl: './inspect-volunteer.component.html',
  styleUrls: ['./inspect-volunteer.component.css']
})
export class InspectVolunteerComponent implements OnInit {

  @Input() volunteer!: Volunteer;
  
  

  constructor(
    public activeModal: NgbActiveModal, 
    public modalService: NgbModal,
    private volunteerService: VolunteerService,
    private router: Router,
    private route: ActivatedRoute,) { }

  ngOnInit(): void {
    this.volunteer = new Volunteer(); 
    this.route.paramMap.subscribe(params => {
      const volunteerId = Number(params.get('idvoluntaria'));
      if (volunteerId) {
        this.volunteerService.findVolunteer(volunteerId).subscribe({
          next: (response) => this.volunteer= response,
          error: (e) => {
            SwalFacade.error("Ocorreu um erro! Redirecionando para a listagem", e)
            this.router.navigate(['/voluntaria/voluntarias'])
          },
        });
      }
    });
  }

  /**
   * @description Abre o modal de edição
   * @param volunteer objeto da voluntária para ir como variavel no componente
   */
  editVolunteer(volunteer: Volunteer) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    let modalRef = this.modalService.open(EditVolunteerComponent, { size: 'xl' })
    modalRef.componentInstance.volunteer = Volunteer;  // Passando a voluntaria
    modalRef.componentInstance.editMode = true;          // Passando o modo de edição
  }

  /**
   * @description Abre o modal de exclusão
   * @param volunteer objeto da voluntária para ir como variavel no componente
   */
  deleteVolunteer(volunteer: Volunteer) {
    this.activeModal.close(); // Fecha o modal atual de visualização
    this.modalService.open(
      DeleteVolunteerComponent, { size: 'xl' }
    ).componentInstance.volunteer = volunteer;
  }

}
