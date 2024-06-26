import { Component, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Volunteer, VolunteerPOST } from 'src/app/shared/models/volunteer/volunteer.model';
import { VolunteerService } from 'src/app/volunteer/services/volunteer.service';
import { CreateVolunteerComponent, DeleteVolunteerComponent, EditVolunteerComponent, InspectVolunteerComponent } from '../index';


@Component({
  selector: 'app-list-volunteer',
  templateUrl: './list-volunteer.component.html',
  styleUrls: ['./list-volunteer.component.css']
})
export class ListVolunteerComponent implements OnInit, OnDestroy {

  volunteers!: Volunteer[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private modalService: NgbModal, private volunteerService: VolunteerService) { }

  ngOnInit(): void {
    this.listVolunteers(false); // Inicialmente lista as voluntárias.
    // Se inscreve no Observable de atualização. Quando um novo valor é emitido, chama a listagem novamente.
    this.subscription = this.volunteerService.refreshPage$.subscribe(() => {
      this.listVolunteers(false); // Lista os beneficiados novamente para refletir as atualizações.
    })
  }

  ngOnDestroy(): void {
    // Cancela a subscrição para evitar vazamentos de memória.
    this.subscription?.unsubscribe();
  }

  /**
   * @description Lista todas as voluntárias no componente
   * @param isFiltering boolean que indica se a listagem será filtrada ou não
   */
  listVolunteers(isFiltering: boolean) {
    this.isLoading = true; // Flag de carregamento
    this.volunteerService.listVolunteer().subscribe({
      next: (response) => {
        this.volunteers = response
        // Ordena por nome crescente
        this.volunteers.sort((a, b) => (a.user!.name ?? '').localeCompare(b.user!.name ?? ''))
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => {
        if (isFiltering) {
          this.volunteers = this.volunteers.filter(
            (volunteers: Volunteer) => {
              // Asegura que name é uma string antes de chamar métodos de string
              return volunteers.user!.name! ? volunteers.user!.name!.toLowerCase().includes(this.filter.toLowerCase()) : false;
            }
          );
        }
        this.isLoading = false;
      }
    })

  }

  /**
   * @description Verifica se o usuário está filtrando dados e chama os métodos
   * @param event Um evento do input
   */
  filterVolunteer(event: Event) {
    if (event != undefined) {
      this.volunteers = []; // Esvazia o array

      // A ideia tem que ser se tiver string então filtrar 
      if (this.filter != '') {
        this.listVolunteers(true)
      } else {
        // se não tiver então a gente filtra tudo
        this.listVolunteers(false);
      }
    }
  }

  /**
   * @description Abre o modal de inspeção
   * @param volunteer objeto do voluntária para ir como variavel no componente
   */
  inspectVolunteer(volunteer: Volunteer) {
    let modalRef = this.modalService.open(InspectVolunteerComponent, { size: 'xl' });
    modalRef.componentInstance.volunteer = volunteer;    // Passando o voluntária
  }

  /**
   * @description Abre o modal de criação
   */
  newVolunteer() {
    this.modalService.open(CreateVolunteerComponent, { size: 'xl' });
  }

  /**
   * @description Abre o modal de edição
   * @param volunteer objeto do voluntária para ir como variavel no componente
   */
  editVolunteer(volunteer: Volunteer) {
    let volunteerPOST = new VolunteerPOST();
    volunteerPOST.transformObjectToEdit(volunteer);
    let modalRef = this.modalService.open(EditVolunteerComponent, { size: 'xl' })
    modalRef.componentInstance.volunteer = volunteerPOST;  // Passando o voluntária
    modalRef.componentInstance.editMode = true;          // Passando o modo de edição
    modalRef.componentInstance.countrySelected = volunteer.city?.state?.country?.id;  // Passando a voluntaria
    modalRef.componentInstance.stateSelected = volunteer.city?.state?.id;          // Passando o modo de edição
  }

  /**
   * @description Abre o modal de exclusão
   * @param volunteer objeto do voluntária para ir como variavel no componente
   */
  deleteVolunteer(volunteer: Volunteer) {
    this.modalService.open(
      DeleteVolunteerComponent, { size: 'xl' }
    ).componentInstance.volunteer = volunteer;
  }

}
